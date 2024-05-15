import csv
import re

def extract_dates(dates_str):
    date_parts = []
    dates = [date.strip() for date in dates_str.split(';')]  # Sépare les dates par ';'
    
    for date in dates:
        parts = date.split('/')
        day = int(parts[0]) if parts[0].isdigit() else None  # Jour (converti en int si possible)
        month = int(parts[1]) if parts[1].isdigit() else None  # Mois (converti en int si possible)
        year = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else None  # Année (converti en int si possible)
        
        date_parts.append([day, month, year])
    
    return date_parts

def read_csv_data(file_path):
    first_names = []
    important_names = []
    date_parts_list = []  # Liste de listes pour les parties de date
    misc_items = []

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            first_names.append(row['First Name'])
            important_names.extend([name.strip() for name in row['Important Names'].split(';')])
            
            # Extraction des parties de date
            date_parts = extract_dates(row['Dates'])
            date_parts_list.extend(date_parts)
            
            misc_items.extend([item.strip() for item in row['Misc'].split(';')])
    
    return first_names, important_names, date_parts_list, misc_items

def format_dates(dates):
    dates_list = []
    formatted_date=""
    for d in dates:
        if len(d)==4 :
            formatted_date = d[2:]
            dates_list.append(formatted_date)

        formatted_date = str(int(d)) # remove leading 0
        dates_list.append(formatted_date)

    return dates_list


# Example usage:
file_path = 'data.csv'
first_names, important_names, dates, misc_items = read_csv_data(file_path)

#print(format_dates(dates))

print("First Names:", first_names)
print("Important Names:", important_names)
print("Dates:", dates)
print("Miscellaneous Items:", misc_items)
