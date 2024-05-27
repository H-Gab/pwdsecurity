from extractInformations import read_csv_data,format_dates

def creat_possible_date():

    _, _, dates, _ = read_csv_data('data.csv')

    dates = format_dates(dates)
    
    #print(dates,'\n\n')

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

    #print(all_possibility)
    return all_possibility

creat_possible_date()



