import argparse
import os
import uuid
from leet import leet
from date import creat_possible_date
from itertools import product

def main(): #Ajouter args plus tard

    special_chars= [ #according IBM
    '!',
    '(',
    ')',
    '-',
    '.',
    '?',
    '[',
    ']',
    '_',
    '`',
    '~',
    ';',
    ':',
    '@',
    '#',
    '$',
    '%',
    '^',
    '&',
    '*',
    '+',
    '=']
    
    # Generate a unique output file name
    file_name = f"output_{uuid.uuid4().hex}.txt"
    file_path = os.path.join('.', file_name)

    combinations=[]

    names = leet()
    dates = creat_possible_date()  

    # Generate all combinations of names, dates, and special characters
    all_combinations = []
    for name, date, special_char in product(names, dates, special_chars):
        # Concatenate name, date, and special character in different combinations
        combinations = [
            f"{special_char}{name}{date}",  # Special char + name + date
            f"{name}{special_char}{date}",  # Name + special char + date
            f"{name}{date}{special_char}"   # Name + date + special char
        ]
        all_combinations.extend(combinations)

    for idx, combination in enumerate(all_combinations, start=1):
        combinations.append(combination)
        print(f"Combination {idx}: {combination}")

    with open(file_path, 'w') as file:
        for pwd in combinations:
            file.write(str(pwd)+'\n')

    print(f"Content successfully written to '{file_path}'.")

    print("Text")  # Continue with additional logic as needed

main()

'''
if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Description of your script.")

    # Add arguments to the parser
    parser.add_argument('arg1', type=str, default='none', help='Leet (-l [none,basic,complex], default none)')
    parser.add_argument('--option1', type=int, default=0, help='Description of option 1')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(args)
'''