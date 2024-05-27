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
        
        if important_names and any(name.strip() for name in important_names):
            names = first_names + important_names
        else:
            names = first_names
    elif (args.leet == 'simple'):
        names = leet('csv/leet_basic.csv','simple')
    elif (args.leet == 'basic'):
        names = leet('csv/leet_basic.csv','all')
    elif (args.leet == 'complex'):
        names = leet('csv/leet_complex.csv','all')
    
    #print(names)
    dates = creat_possible_date()  
    _,_,_,misc = read_csv_data('data.csv')

    if (args.verbose):
        print(names)
        print(dates)
        print(misc)

    response = 'n'
    if (args.time) :
        print(len(misc))
        print(len(dates))
        print(len(names))
        a = 0
        if (args.special_characters):
            a += len(names) * len(dates) * len(special_chars) * 3
            if (args.misc):
                a += len(names) * len(misc) * len(special_chars) * 3
                a += len(misc) * len(dates) * len(special_chars) * 3
        else : 
            if (args.misc):
                a += len(misc) * len(dates) * 2
                a += len(names) * len(misc) * 2

        a += len(names) * len(dates) * 2
        if (not args.verbose):
            t = a/1000000
        else :
            t = a/7500
        
        size = a*(110000000/8100000)
        print(f"Estimated time of creation : {t}s; Estimated number of combination : {a}; Estimated size of file : {int(size)}o")
        response = input("Do you want to start? (y/n): ")

    if(not args.time or response.lower() == 'y') :
        start_time =time.time()
        # Generate all combinations
        all_combinations = []
        if (args.special_characters):
            if (args.misc):
                unique_combinations = set()
                for name, date, special_char in product(names, dates, special_chars):
                    # Concatenate name, date, and special character in different combinations
                    combinations = [
                        f"{special_char}{name}{date}",  
                        f"{name}{special_char}{date}", 
                        f"{name}{date}{special_char}",
                    ]
                    all_combinations.extend(combinations)
                for date, special_char,misc in product(dates, special_chars,misc):
                    # Concatenate name, date, and special character in different combinations
                    combinations = [
                        f"{special_char}{misc}{date}",  
                        f"{misc}{special_char}{date}", 
                        f"{misc}{date}{special_char}"
                    ]
                    all_combinations.extend(combinations)
                for name, special_char,misc in product(names, special_chars,misc):
                    # Concatenate name, date, and special character in different combinations
                    combinations = [
                        f"{special_char}{name}{misc}",  
                        f"{name}{special_char}{misc}", 
                        f"{name}{misc}{special_char}"
                    ]
                    all_combinations.extend(combinations)
                
            else :
                for name, date, special_char in product(names, dates, special_chars):
                    # Concatenate name, date, and special character in different combinations
                    combinations = [
                        f"{special_char}{name}{date}",  
                        f"{name}{special_char}{date}", 
                        f"{name}{date}{special_char}"   
                    ]
                    all_combinations.extend(combinations)

        if (args.misc):
            unique_combinations = set()  
            for name, arg  in product(names, misc):
                # Concatenate name, date, and special character in different combinations
                combinations = [
                    f"{arg}{name}",  
                    f"{name}{arg}", 
                ]
                unique_combinations.update(combinations)  # Add combinations to the set
            all_combinations.extend(list(unique_combinations))

            for misc, date in product(misc, dates):
                # Concatenate name, date, and special character in different combinations
                combinations = [
                    f"{date}{misc}",  
                    f"{name}{date}",  
                ]
                all_combinations.extend(combinations)

        for name, date in product(names, dates):
                # Concatenate name, date, and special character in different combinations
                combinations = [
                    f"{date}{name}",  
                    f"{name}{date}",  
                ]
                all_combinations.extend(combinations)
            

        if (args.verbose):
            for idx, combination in enumerate(all_combinations, start=1):
                combinations.append(combination)
                print(f"Combination {idx}: {combination}")

        for idx, combination in enumerate(all_combinations, start=1):
                combinations.append(combination)
        with open(file_path, 'w') as file:
            for pwd in combinations:
                file.write(str(pwd)+'\n')
        
        end_time=time.time()
        total_time = end_time - start_time
        print(f"Time of Execution : '{total_time}'.")
        print(f"Content successfully written to '{file_path}'.")
        if (args.compare != 'none'):
            if args.compare in all_combinations:
                print(f"The password '{args.compare}' is in the list of combinations.")
            else:
                print(f"The password '{args.compare}' is NOT in the list of combinations.")

        


#main()


if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Creation of a list of possible password using personal information.")

    # Add arguments to the parser
    parser.add_argument('-l', '--leet', type=str, default='none', help='Leet level (-l [none,basic,complex], default none)')
    parser.add_argument('-sc', '--special_characters', action='store_true', help='Enable special characters if flag is present')
    parser.add_argument('-t', '--time', action='store_true', help='Enable special characters if flag is present')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable the verbose')
    parser.add_argument('-m', '--misc', action='store_true', help='Enable the miscellaneous')
    parser.add_argument('-c', '--compare', type=str, default='none', help='Compare your password with the created dictionary')
    #parser.add_argument('--option1', type=int, default=0, help='Description of option 1')

    # Parse the command-line arguments
    args = parser.parse_args()
    print(args)
    # Call the main function with parsed arguments
    main(args)
