import csv
with open ('data.csv','r') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    for i in data:
        print(i)