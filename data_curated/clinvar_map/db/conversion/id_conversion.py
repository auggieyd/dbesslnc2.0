import requests
import pandas as pd
import time
import json


# Read the file containing lncBookID and noncodeID
def read_ids(file_path):
    df = pd.read_csv(file_path)
    return df['lncRNA_id'].dropna().astype(str).tolist()


# Send requests in batches of 200 IDs
def send_request(ids_batch):
    url = "https://ngdc.cncb.ac.cn/lncbook/conversion"
    ids_str = "\n".join(ids_batch)
    payload = {'ids': ids_str}
    try:
        response = requests.post(url, data=payload, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed, status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None


def _concat_unique(series, sep="|"):
    vals = [str(x) for x in series if pd.notna(x) and str(x) != "N/A" and str(x) != "" and str(x) != "-"]
    if not vals:
        return ""
    return sep.join(pd.unique(pd.Series(vals)))


# Process the request results and save them to a CSV file
def process_and_save_results(results, output_file, group_by=None, sep="|"):
    rows = []
    for result in results:
        if not result:
            continue
        for entry in result:
            lncbook_id = entry.get("geneid", "N/A")
            noncode_id = entry.get("noncode", "N/A")
            symbol = entry.get("symbol", "N/A")
            ensembl_id = entry.get("gencode", "N/A")
            ncbi_id = entry.get("entrez", "N/A")
            rows.append(
                {
                    "lncbook_id": lncbook_id,
                    "noncode_id": noncode_id,
                    "symbol": symbol,
                    "ensembl_id": ensembl_id,
                    "ncbi_id": ncbi_id,
                }
            )

    if not rows:
        print(f"No results to save for {output_file}")
        return

    df = pd.DataFrame(rows)
    df_out = df.drop_duplicates()

    if group_by and group_by in df.columns:
        agg_dict = {
            col: (lambda s, c=col: _concat_unique(s, sep=sep)) for col in df.columns if col != group_by
        }
        df_out = df.groupby(group_by, as_index=False).agg(agg_dict)  

    df_out.to_csv(output_file, index=False)
    print(f"Saved conversion results to {output_file}")


# Main function
def main(lncBook_file, noncode_file, output_file_lncbook, output_file_noncode):
    # Read IDs
    lncBook_ids = read_ids(lncBook_file)
    noncode_ids = read_ids(noncode_file)

    # Process lncbook id
    print("Processing lncbook id...")
    lncBook_results = []
    for i in range(0, len(lncBook_ids), 200):
        ids_batch = lncBook_ids[i:i + 200]
        print(f"Sending batch {i // 200 + 1} of lncbook id requests...")
        result = send_request(ids_batch)
        lncBook_results.append(result)
        time.sleep(1)

    # Process noncode id
    print("Processing noncode id...")
    noncode_results = []
    for i in range(0, len(noncode_ids), 200):
        ids_batch = noncode_ids[i:i + 200]
        print(f"Sending batch {i // 200 + 1} of noncode id requests...")
        result = send_request(ids_batch)
        noncode_results.append(result)
        time.sleep(1)

    # Save lncbook results
    print(f"Saving lncbook conversion results to {output_file_lncbook}")
    process_and_save_results(lncBook_results, output_file_lncbook, group_by=None)

    # Save noncode results
    print(f"Saving noncode conversion results to {output_file_noncode}")
    process_and_save_results(noncode_results, output_file_noncode, group_by="noncode_id", sep=";")


# Call the main function
if __name__ == "__main__":
    lncBook_file = '../statistic/lncbook_lncRNA.csv'
    noncode_file = '../statistic/noncode_lncRNA.csv'
    output_file_lncbook = 'lncbook_conversion_results.csv'
    output_file_noncode = 'noncode_conversion_results.csv'

    main(lncBook_file, noncode_file, output_file_lncbook, output_file_noncode)
