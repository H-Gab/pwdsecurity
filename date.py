from extractInformations import read_csv_data,format_dates

def creat_possible_date(dates):
    all_possibility=[]
    for d in dates :
        for a in d[0] :
            for b in d[1]:
                all_possibility.append(a+b)
                all_possibility.append(b+a)

        if d[2] != None :
            for a in d[0] :
                for b in d[1]:
                    for c in d[2]: 
                        all_possibility.append(a+b+c)
                        all_possibility.append(c+b+a)
                        all_possibility.append(c+a+b)
                        all_possibility.append(b+a+c)
                        all_possibility.append(c+b)
                        all_possibility.append(b+c)
    return all_possibility



file_path = 'data.csv'
first_names, important_names, dates, misc_items = read_csv_data(file_path)
print(format_dates(dates))
date= format_dates(dates)
print(creat_possible_date(date))