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

def generate_leet_alternatives(name, leet_mapping, mode):
    name = name.lower()
    
    if mode == 'simple':
        leet_alternatives = set([name])  # Start with the original name in a set to avoid duplicates
        for i, char in enumerate(name):
            if char in leet_mapping:
                leet_equivalents = leet_mapping[char]
                for leet_char in leet_equivalents:
                    # Create a new alternative by replacing the character at position i
                    new_name = name[:i] + leet_char + name[i+1:]
                    leet_alternatives.add(new_name)
    
    else:
        leet_alternatives = [""]
        for char in name:
            if char in leet_mapping:
                leet_equivalents = leet_mapping[char]
            else:
                leet_equivalents = [char]
            
            leet_alternatives = [combo + substitute for combo in leet_alternatives for substitute in leet_equivalents]

    return list(leet_alternatives)

def generate_leet_alternatives_for_names(names_list, file, mode):
    leet_mapping = import_mapping(file)

    all_leet_alternatives = {}
    for name_group in names_list:
        for name in name_group:
            alternatives = generate_leet_alternatives(name, leet_mapping, mode)
            all_leet_alternatives[name] = alternatives

    return all_leet_alternatives

def leet(leet_file,mode) :
    file = leet_file  
    leets = []

    first_names, important_names,_,_ = read_csv_data('data.csv')
    names = first_names+important_names
    
    names = possible_variations(names)
    

    # Generate leet alternatives for the name
    name_to_leet_alternatives = generate_leet_alternatives_for_names(names, file, mode)

    # Print the generated alternatives for each name
    for name, alternatives in name_to_leet_alternatives.items():
        #print(f"Leet alternatives for '{name}':")
        for alternative in alternatives:
            leets.append(alternative)  
        #print(leets)
    return leets

leet('csv/leet_basic.csv','all') # Uncomment this to test