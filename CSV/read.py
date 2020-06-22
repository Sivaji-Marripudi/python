# read csv file
import csv
with open ('data.csv','r') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    for i in data:
        print(i)

# read specific row in csv file and print its content
import csv
with open('data.csv','r') as csv_file:
    data = csv.DictReader(csv_file)
    for i in data:
        print(i['beat'],i['grid'])