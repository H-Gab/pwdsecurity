import csv
import re

def extract_dates(dates_str):
    date_parts = []
    dates = [date.strip() for date in dates_str.split(';')]
    
    for date in dates:
        parts = date.split('-')
        day = parts[2] if parts[2].isdigit() else None  
        month = parts[1] if parts[1].isdigit() else None  
        year = parts[0] if parts[0]!="0000" and parts[0].isdigit() else None 
        
        date_parts.append([day, month, year])
    
    return date_parts

def read_csv_data(file_path):
    first_names = []
    important_names = []
    date_parts_list = [] 
    misc_items = []

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            first_names.append(row['First Name'])
            important_names.extend([name.strip() for name in row['Important Names'].split(';')])
            
            # Extract dates parts
            date_parts = extract_dates(row['Dates'])
            date_parts_list.extend(date_parts)
            
            misc_items.extend([item.strip() for item in row['Misc'].split(';')])
    
    return first_names, important_names, date_parts_list, misc_items

def format_dates(dates):
    all_dates_list = []
    formatted_date=""
    print(formatted_date)
    for d in dates:
        dates_list = []
        day = d[0]
        if str(int(day)) != day :
            dates_list.append([day,str(int(day))])
        else :
            dates_list.append([day])

        month = d[1]
        if str(int(month)) != month :
            dates_list.append([month,str(int(month))])
        else :
            dates_list.append([month])

        year = d[2]
        if year != None :
            dates_list.append([year,str(year)[2:]])
        else :
            dates_list.append(None)
            

        #formatted_date = str(int(d)) # remove leading 0
        all_dates_list.append(dates_list)

    return all_dates_list

'''
file_path = 'data.csv'
first_names, important_names, dates, misc_items = read_csv_data(file_path)

print(format_dates(dates))
print("First Names:", first_names)
print("Important Names:", important_names)
print("Dates:", dates)
print("Miscellaneous Items:", misc_items)
'''

