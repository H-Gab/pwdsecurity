import csv
from extractInformations import read_csv_data
first_names, important_names,_,_ = read_csv_data('data.csv')


def find_nicknames(csv_file, target_name):
    nicknames = []

    target_name = target_name.lower().replace(" ", "")
    nicknames.append(target_name)

    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            first_name = row[0].strip()

            if target_name == first_name:
                nicknames.extend([name.strip() for name in row[1:] if name.strip() != target_name])

    return nicknames

def possible_variations(names):
    all_possible_nicknames = []

    for n in names:
        nicknames = find_nicknames('csv/names.csv', n)
        unique_nicknames = list(set(nicknames))  # Remove duplicates from nicknames list
        all_possible_nicknames.append(unique_nicknames)

    return all_possible_nicknames

names = first_names+important_names
print(possible_variations(names))