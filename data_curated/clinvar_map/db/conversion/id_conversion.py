import requests
import pandas as pd
import time
import json


# Read the file containing lncBookID and NONCODEID
def read_ids(file_path):
    with open(file_path, 'r') as file:
        ids = file.read().splitlines()
    return ids


# Send requests in batches of 200 IDs
def send_request(ids_batch):
    # LncBook conversion API URL
    url = "https://ngdc.cncb.ac.cn/lncbook/conversion"

    # Combine IDs into a format suitable for the request
    ids_str = "\n".join(ids_batch)

    # Set the request payload
    payload = {'ids': ids_str}

    # Send POST request
    response = requests.post(url, data=payload)

    # Return results if the request is successful
    if response.status_code == 200:
        return json.loads(response.text)  # Parse as JSON
    else:
        print(f"Request failed, status code: {response.status_code}")
        return None


# Process the request results and save them to a CSV file, keeping ID, symbol, and entrez fields
def process_and_save_results(id, results, output_file):
    # Store results in a list to prepare for writing to CSV
    data = []

    for i, result in enumerate(results):
        if result:
            for entry in result:
                # Extract ID, symbol, and entrez fields
                geneID = entry.get(id, "N/A")
                symbol = entry.get("symbol", "N/A")
                entrez = entry.get("entrez", "N/A")
                data.append([geneID, symbol, entrez])

    # Create DataFrame and save it as a CSV file
    df = pd.DataFrame(data, columns=["id", "symbol", "entrez"])
    df = df.drop_duplicates(subset=df.columns[0])

    # Save as CSV file
    df.to_csv(output_file, index=False)
    print(f"Saved conversion results to {output_file}")


# Main function
def main(lncBook_file, NONCODE_file, output_file_lncbook, output_file_noncode):
    # Read IDs
    lncBook_ids = read_ids(lncBook_file)
    NONCODE_ids = read_ids(NONCODE_file)

    # Process lncBookID
    print("Processing lncBookID...")
    lncBook_results = []
    for i in range(0, len(lncBook_ids), 200):
        ids_batch = lncBook_ids[i:i + 200]
        print(f"Sending batch {i // 200 + 1} of lncBookID requests...")
        result = send_request(ids_batch)
        lncBook_results.append(result)
        time.sleep(1)  # Delay 1 second to avoid frequent requests

    # Process NONCODEID
    print("Processing NONCODEID...")
    noncode_results = []
    for i in range(0, len(NONCODE_ids), 200):
        ids_batch = NONCODE_ids[i:i + 200]
        print(f"Sending batch {i // 200 + 1} of NONCODEID requests...")
        result = send_request(ids_batch)
        noncode_results.append(result)
        time.sleep(1)  # Delay 1 second to avoid frequent requests

    # Save lncBookID results
    print(f"Saving lncBookID conversion results to {output_file_lncbook}")
    process_and_save_results("geneid", lncBook_results, output_file_lncbook)

    # Save NONCODEID results
    print(f"Saving NONCODEID conversion results to {output_file_noncode}")
    process_and_save_results("noncode", noncode_results, output_file_noncode)

# Call the main function
if __name__ == "__main__":
    lncBook_file = 'lncbook_ids.txt'  # Replace with the actual path to lncBookID file
    NONCODE_file = 'noncode_ids.txt'  # Replace with the actual path to NONCODEID file
    output_file_lncbook = 'lncbook_conversion_results.csv'  # Output file path for lncBook results
    output_file_noncode = 'noncode_conversion_results.csv'  # Output file path for NONCODE results

    main(lncBook_file, NONCODE_file, output_file_lncbook, output_file_noncode)
