import requests
import xml.etree.ElementTree as ET
import time
import csv

# Input file: each line contains one RCV accession
INPUT_FILE = "marked_rcv_ids.txt"
# Output file: tab-separated values
OUTPUT_FILE = "rcv_conditions.txt"

def fetch_conditions(rcv_id):
    """
    Fetch associated conditions for a given RCV accession using efetch with rettype=clinvarset.
    """
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    fetch_params = {
        "db": "clinvar",
        "id": rcv_id,
        "rettype": "clinvarset",
        "retmode": "xml"
    }

    try:
        response = requests.get(fetch_url, params=fetch_params, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return f"FETCH_ERROR: {e}"

    # Parse XML and extract all trait (condition) names
    try:
        root = ET.fromstring(response.text)
        conditions = set()

        for trait_set in root.findall(".//TraitSet"):
            for trait in trait_set.findall("Trait"):
                for name in trait.findall("Name"):
                    for ev in name.findall("ElementValue"):
                        if ev.text:
                            conditions.add(ev.text.strip())

        return ";".join(sorted(conditions)) if conditions else "N/A"

    except ET.ParseError as e:
        return f"XML_PARSE_ERROR: {e}"

def main():
    with open(INPUT_FILE, "r") as infile, open(OUTPUT_FILE, "w", newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter="\t")
        writer.writerow(["RCV", "Conditions"])

        for line in infile:
            rcv = line.strip()
            if not rcv:
                continue
            conditions = fetch_conditions(rcv)
            writer.writerow([rcv, conditions])
            time.sleep(0.4)  # NCBI rate limit: ~3 requests/second

if __name__ == "__main__":
    main()
