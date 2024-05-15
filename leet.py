import csv
from names import possible_variations
from extractInformations import read_csv_data
from itertools import product

def import_mapping(file):
    leet_mapping = {}

    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            char = row[0]
            leet_equivalents = row[1:]
            leet_equivalents.append(char)
            leet_mapping[char] = leet_equivalents

    return leet_mapping

def generate_leet_alternatives(name, leet_mapping):
    name = name.lower()

    # Generate all possible leet alternatives
    leet_alternatives = [""]
    for char in name:
        if char in leet_mapping:
            leet_equivalents = leet_mapping[char]

        leet_alternatives = [combo + substitute for combo in leet_alternatives for substitute in leet_equivalents]

    return leet_alternatives

def generate_leet_alternatives_for_names(names_list, file):
    leet_mapping = import_mapping(file)

    all_leet_alternatives = {}
    for name_group in names_list:
        for name in name_group:
            alternatives = generate_leet_alternatives(name, leet_mapping)
            all_leet_alternatives[name] = alternatives

    return all_leet_alternatives

def leet() :
    file = 'csv/leet_basic.csv'  
    leets = []

    first_names, important_names,_,_ = read_csv_data('data.csv')
    names = first_names+important_names
    
    names = possible_variations(names)
    

    # Generate leet alternatives for the name
    name_to_leet_alternatives = generate_leet_alternatives_for_names(names, file)

    # Print the generated alternatives for each name
    for name, alternatives in name_to_leet_alternatives.items():
        print(f"Leet alternatives for '{name}':")
        for alternative in alternatives:
            leets.append(alternative)  
        print(leets)

leet() # Uncomment this to test