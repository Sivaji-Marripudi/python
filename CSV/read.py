import csv
with open("data.csv","r") as csvfile:
    csv_file = csv.reader(csvfile)
    for data in csv_file:
        print(data)