# -*- coding: utf-8 -*-
import re
import csv

# --- 1. Rule Set Definition --
# This dictionary centralizes all rules for easy management and interpretation.
RULES = {
    "LEXICON": {
        "SEVERITY": r'(severe|acute|fulminant|progressive|malignant)',
        "EARLY_ONSET": r'(neonatal|infantile|congenital)',
        "CRITICAL_SYSTEMS": r'(encephalopathy|cardiomyopathy|failure|leukodystrophy|leukoencephalopathy|atrophy|atresia|agenesis)',
        "CATASTROPHIC_FINDINGS": r'(brainstem anomalies|high lactate|pyloric atresia)'
    },
    "CONFIRMED": {
        "absolute_keywords": ['lethal', 'fatal', 'thanatophoric', 'hydrops fetalis'],
        "unambiguous_syndromes": [
            'achondrogenesis', 'zellweger syndrome', 'walker-warburg', 'meckel syndrome', 'meckel-gruber',
            'neu-laxova', 'pena-shokeir', 'fowler syndrome', 'alpers-huttenlocher', 'alpers syndrome',
            'menkes disease', 'krabbe disease', 'tay-sachs', 'sandhoff disease', 'canavan disease',
            'wolman disease', 'niemann-pick disease, type a', 'herlitz', 'restrictive dermopathy', 
            'hydrolethalus syndrome', 'gracile syndrome', 'rhabdoid tumor', 'leigh syndrome', 'leigh-like',
            'atypical teratoid rhabdoid tumor', # Exception for 'atypical'
            'glycine encephalopathy', 'nonketotic hyperglycinemia',
            'alveolar capillary dysplasia', 'pontocerebellar hypoplasia, type 2', 'infantile neuroaxonal dystrophy',
            'inad', 'ethylmalonic encephalopathy', 'arc syndrome'
        ]
    },
    "HIGH_SEVERITY": {
        "Severe_Immunodeficiency": ['severe combined immunodeficiency', 'scid', 'hemophagocytic lymphohistiocytosis', 'fhl'],
        "High_Risk_Cardiac": ['arrhythmogenic', 'long qt syndrome', 'brugada syndrome', 'catecholaminergic polymorphic ventricular tachycardia', 'cpvt', 'pulmonary arterial hypertension', 'marfan syndrome', 'loeys-dietz syndrome', 'ehlers-danlos syndrome, vascular type', 'aortic dissection'],
        "Progressive_Systemic_Disorder": ['cystic fibrosis', 'duchenne muscular dystrophy', 'ataxia-telangiectasia', 'fanconi anemia', 'dyskeratosis congenita'],
        "Severe_Metabolic_Crisis_Risk": ['urea cycle', 'maple syrup urine disease', 'msud', 'propionic acidemia', 'methylmalonic acidemia', 'glutaric aciduria type 1', 'mcad', 'vlcad', 'lchad deficiency', 'mitochondrial trifunctional protein deficiency', 'salt-wasting'],
        "High_Variability_Syndrome": ['niemann-pick disease, type c', 'gaucher disease, type 3', 'adams-oliver syndrome', 'diaphragmatic hernia', 'hypoplastic left heart syndrome', 'renal agenesis', 'renal aplasia'],
        "Heritable_Malignancy": ['cancer', 'carcinoma', 'sarcoma', 'leukemia', 'lymphoma', 'blastoma', 'glioma', 'melanoma', 'malignant']
    },
    "EXCLUSIONS": {
        "rule_zero_modifiers": ['mild', 'atypical', 'incomplete', 'partial', 'delayed onset', '-induced', 'drug-associated', 'exercise-induced', 'in situ', 'unilateral', 'equivocal'],
        "rule_zero_risk_status": ['susceptibility to', 'predisposition', 'risk', 'family history of', 'finding'],
        "general_exclusions": ['modifier of', 'resistance to', 'protection against', 'response to', 'polymorphism'],
        "non_lethal_diseases": [
            'achondroplasia', 'huntington disease', 'alzheimer disease', 'parkinson disease',
            'benign familial', 'phenylketonuria', 'galactosemia', 'biotinidase deficiency',
            'rett syndrome', 'angelman syndrome', 'prader-willi', 'sweat chloride elevation'
        ]
    }
}
# --- 2. NEW Smart Splitting Function ---
def smart_split(line):
    """
    Splits a string by semicolons, but ignores semicolons inside parentheses.
    This correctly handles cytogenetic notations like t(9;22).
    """
    parts = []
    paren_depth = 0
    current_part_start = 0
    for i, char in enumerate(line):
        if char == '(':
            paren_depth += 1
        elif char == ')':
            paren_depth = max(0, paren_depth - 1) # Avoid negative depth on mismatched parentheses
        elif char == ';' and paren_depth == 0:
            parts.append(line[current_part_start:i])
            current_part_start = i + 1
    # Add the last part of the string
    parts.append(line[current_part_start:])
    return parts

def classify_phenotype_final(phenotype_string, rules):
    """
    Classifies a phenotype into 'Confirmed Lethal', 'High Severity', or 'Non-Severe'
    based on the final, refined rule set.
    """
    lower_pheno = phenotype_string.lower()

    # --- 0. Highest Priority Exclusion Rules (Rule Zero) ---
    # Smart handling of non-lethal modifiers like 'mild' and 'atypical'
    non_lethal_modifiers = rules['EXCLUSIONS']['rule_zero_modifiers']
    
    # Exemption for the phrase 'with mild'
    if 'with mild' in lower_pheno:
        if 'mild' in non_lethal_modifiers: non_lethal_modifiers.remove('mild')
    
    # Exemption for AT/RT, which contains 'atypical' in its name
    if 'atypical teratoid rhabdoid tumor' in lower_pheno:
        if 'atypical' in non_lethal_modifiers: non_lethal_modifiers.remove('atypical')
            
    # If a modifier is found, check for conflict with a top-tier term
    found_modifier = next((mod for mod in non_lethal_modifiers if mod in lower_pheno), None)
    if found_modifier:
        top_tier_keywords = rules['CONFIRMED']['absolute_keywords'] + rules['CONFIRMED']['unambiguous_syndromes']
        has_top_tier_conflict = any(kw in lower_pheno for kw in top_tier_keywords)
        if has_top_tier_conflict:
            return 'High Severity', 'Conflicting Modifiers', f"'{found_modifier}' conflicts with a top-tier lethal term", found_modifier
        else:
            return 'Non-Severe', None, None, None

    # Strict exclusion of risk/susceptibility states, unless it's for high-risk cancer
    if any(keyword in lower_pheno for keyword in rules['EXCLUSIONS']['rule_zero_risk_status']):
        if any(kw in lower_pheno for kw in rules['HIGH_SEVERITY']['Heritable_Malignancy']):
             return 'High Severity', 'Heritable Cancer Syndrome', 'High-penetrance cancer predisposition.', 'risk/susceptibility + cancer'
        else:
            return 'Non-Severe', None, None, None

    # --- 1. General Exclusion and Inclusion Rules ---
    if any(keyword in lower_pheno for keyword in rules['EXCLUSIONS']['general_exclusions']): return 'Non-Severe', None, None, None
    if any(disease in lower_pheno for disease in rules['EXCLUSIONS']['non_lethal_diseases']): return 'Non-Severe', None, None, None

    # --- 2. Inclusion Rules: Confirmed Lethal ---
    all_confirmed_keywords = rules['CONFIRMED']['absolute_keywords'] + rules['CONFIRMED']['unambiguous_syndromes']
    for kw in all_confirmed_keywords:
        if kw in lower_pheno:
            return 'Confirmed Lethal', 'Infantile-Lethal Syndrome', f"Matched top-tier keyword: {kw}", kw

    lexicon = rules['LEXICON']
    if (re.search(lexicon['SEVERITY'], lower_pheno) and re.search(lexicon['EARLY_ONSET'], lower_pheno) and re.search(lexicon['CRITICAL_SYSTEMS'], lower_pheno)):
        return 'Confirmed Lethal', 'Lethal Clinical Pattern', 'Matched pattern: Severe+Early+Systemic', 'pattern: severe+early+systemic'
    if (re.search(lexicon['CRITICAL_SYSTEMS'], lower_pheno) and re.search(lexicon['CATASTROPHIC_FINDINGS'], lower_pheno)):
        return 'Confirmed Lethal', 'Lethal Clinical Pattern', 'Matched pattern: Critical System + Catastrophic Finding', 'pattern: critical+catastrophic'

    # Specific lethal subtype patterns
    if 'osteogenesis imperfecta' in lower_pheno and ('type ii' in lower_pheno or 'perinatal' in lower_pheno): return 'Confirmed Lethal', 'Infantile-Lethal Syndrome', 'osteogenesis imperfecta, lethal type', 'osteogenesis imperfecta, lethal type'
    if 'hypophosphatasia' in lower_pheno and ('infantile' in lower_pheno or 'perinatal' in lower_pheno): return 'Confirmed Lethal', 'Infantile-Lethal Syndrome', 'hypophosphatasia, lethal type', 'hypophosphatasia, lethal type'
    if ('spinal muscular atrophy' in lower_pheno or 'sma' in lower_pheno) and ('type 0' in lower_pheno or 'type i' in lower_pheno or 'werdnig-hoffmann' in lower_pheno): return 'Confirmed Lethal', 'Progressive Neuromuscular Disorder', 'sma, lethal type', 'sma, lethal type'
    if ('pompe disease' in lower_pheno or 'glycogen storage disease, type ii' in lower_pheno) and 'infantile' in lower_pheno: return 'Confirmed Lethal', 'Severe Metabolic Disease', 'pompe, infantile', 'pompe, infantile'
    if 'marfan syndrome' in lower_pheno and 'neonatal' in lower_pheno: return 'Confirmed Lethal', 'Severe Connective Tissue Disorder', 'marfan, neonatal', 'marfan, neonatal'
    if 'osteopetrosis' in lower_pheno and ('infantile' in lower_pheno or 'malignant' in lower_pheno): return 'Confirmed Lethal', 'Severe Skeletal Dysplasia', 'osteopetrosis, malignant infantile', 'osteopetrosis, malignant infantile'
    if 'epidermolysis bullosa' in lower_pheno and 'pyloric atresia' in lower_pheno: return 'Confirmed Lethal', 'Severe Skin Disorder', 'eb with pyloric atresia', 'eb with pyloric atresia'
    if 'diaphragmatic hernia' in lower_pheno and ('tetralogy of fallot' in lower_pheno or 'heart defect' in lower_pheno): return 'Confirmed Lethal', 'Multiple Congenital Anomalies', 'pattern: cdh+chd', 'pattern: cdh+chd'
    if 'urea cycle' in lower_pheno and 'neonatal' in lower_pheno: return 'Confirmed Lethal', 'Severe Metabolic Disease', 'urea cycle, neonatal', 'urea cycle, neonatal'

    # --- 3. Inclusion Rules: High Severity ---
    if 'progressive' in lower_pheno and re.search(lexicon['CRITICAL_SYSTEMS'], lower_pheno):
        return 'High Severity', 'Progressive Critical System Disease', 'Progressive nature implies high risk.', 'pattern: progressive+critical_system'
        
    for category, keywords in rules['HIGH_SEVERITY'].items():
        for kw in keywords:
            if kw in lower_pheno:
                return 'High Severity', category.replace('_', ' '), f"Matched high-risk keyword: {kw}", kw

    return 'Non-Severe', None, None, None

def run_final_classification(input_file='unique_phenotypes.txt', output_file='phenotype_severity_classification_final.tsv'):
    """ Main function for the final, refined classification script. """
    print(f"Starting phenotype analysis with final classification rule set on '{input_file}'...")
    
    results = []
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                stripped_line = line.strip()
                if not stripped_line or stripped_line == '-': continue
                conditions = smart_split(stripped_line)
                for condition in conditions:
                    clean_condition = condition.strip()
                    if not clean_condition: continue
                    
                    classification, category, reason, keyword = classify_phenotype_final(clean_condition, RULES)
                    
                    if classification in ['Confirmed Lethal', 'High Severity']:
                        results.append({
                            'Phenotype': clean_condition,
                            'Severity_Level': classification,
                            'Clinical_Category': category,
                            'Matched_Rule_Or_Pattern': keyword,
                            'Reasoning_Note': reason
                        })
    except FileNotFoundError:
        print(f"\nError: Input file '{input_file}' not found.")
        return

    severity_order = {'Confirmed Lethal': 0, 'High Severity': 1}
    sorted_results = sorted(results, key=lambda x: (severity_order.get(x['Severity_Level'], 99), x['Clinical_Category'] or '', x['Phenotype']))

    # Remove duplicates based on Phenotype, keeping the first occurrence (which will be the highest-confidence classification)
    unique_results = []
    seen_phenotypes = set()
    for item in sorted_results:
        if item['Phenotype'] not in seen_phenotypes:
            unique_results.append(item)
            seen_phenotypes.add(item['Phenotype'])
            
    with open(output_file, 'w', encoding='utf-8', newline='') as f_out:
        writer = csv.writer(f_out, delimiter='\t')
        writer.writerow(['Phenotype', 'Severity_Level', 'Clinical_Category', 'Matched_Rule_Or_Pattern', 'Reasoning_Note'])
        for item in unique_results:
            writer.writerow([item['Phenotype'], item['Severity_Level'], item['Clinical_Category'], item['Matched_Rule_Or_Pattern'], item['Reasoning_Note']])

    confirmed_count = len([r for r in unique_results if r['Severity_Level'] == 'Confirmed Lethal'])
    high_severity_count = len([r for r in unique_results if r['Severity_Level'] == 'High Severity'])

    print("\nAnalysis complete.")
    print(f"Found {confirmed_count} phenotypes classified as 'Confirmed Lethal'.")
    print(f"Found {high_severity_count} phenotypes classified as 'High Severity'.")
    print(f"Total retained phenotypes: {len(unique_results)}")
    print(f"Results saved to '{output_file}' (TSV format).")

# --- Execute Script ---
if __name__ == "__main__":
    run_final_classification()