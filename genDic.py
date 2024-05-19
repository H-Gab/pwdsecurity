import argparse
import os
import uuid
import time
from leet import leet
from date import creat_possible_date
from extractInformations import read_csv_data
from itertools import product

def main(args): #Ajouter args plus tard

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
    
    # Generate file name
    file_name = f"output_{uuid.uuid4().hex}.txt"
    file_path = os.path.join('.', file_name)

    combinations=[]
    if (args.leet == 'none') :
        first_names, important_names,_,_ = read_csv_data('data.csv')
        names=first_names+important_names
    elif (args.leet == 'simple'):
        print("Option not working at the moment")
    elif (args.leet == 'basic'):
        names = leet('csv/leet_basic.csv')
    elif (args.leet == 'complex'):
        names = leet('csv/leet_complex.csv')
    
    print(names)
    dates = creat_possible_date()  

    if (args.time) :
        if (args.special_characters):
            a = len(names) * len(dates) * len(special_chars) * 3
            t = a/7500
        else:
            a = len(names) * len(dates) * 2
            t = a/7500
        print(f"Estimated time of creation : {t}s; Number of combination : {a}")
    else :
        start_time =time.time()
        # Generate all combinations
        if (args.special_characters):
            all_combinations = []
            for name, date, special_char in product(names, dates, special_chars):
                # Concatenate name, date, and special character in different combinations
                combinations = [
                    f"{special_char}{name}{date}",  
                    f"{name}{special_char}{date}", 
                    f"{name}{date}{special_char}"   
                ]
                all_combinations.extend(combinations)
        else :
            all_combinations = []
            for name, date in product(names, dates):
                # Concatenate name, date, and special character in different combinations
                combinations = [
                    f"{date}{name}",  
                    f"{name}{date}",  
                ]
                all_combinations.extend(combinations)

        for idx, combination in enumerate(all_combinations, start=1):
            combinations.append(combination)
            print(f"Combination {idx}: {combination}")

        with open(file_path, 'w') as file:
            for pwd in combinations:
                file.write(str(pwd)+'\n')
        
        end_time=time.time()
        total_time = end_time - start_time
        print(f"Time of Execution : '{total_time}'.")
        print(f"Content successfully written to '{file_path}'.")

#main()


if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Description of your script.")

    # Add arguments to the parser
    parser.add_argument('-l', '--leet', type=str, default='none', help='Leet level (-l [none,basic,complex], default none)')
    parser.add_argument('-sc', '--special_characters', action='store_true', help='Enable special characters if flag is present')
    parser.add_argument('-t', '--time', action='store_true', help='Enable special characters if flag is present')
    parser.add_argument('arg1', type=str, default='none', help='Leet (-l [none,basic,complex], default none)')
    #parser.add_argument('--option1', type=int, default=0, help='Description of option 1')

    # Parse the command-line arguments
    args = parser.parse_args()
    print(args)
    # Call the main function with parsed arguments
    main(args)
