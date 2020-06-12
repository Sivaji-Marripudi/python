import csv
with open("data.csv","r") as csvfile:
    csv_file = csv.reader(csvfile)
    with open("new_data.csv","w") as new_csvfile:
        csv_writer = csv.writer(new_csvfile)
        for data in csv_file:
            csv_writer.writerow(data)
# read new_data.csv file
'''
with open('new_data.csv','r') as csvfile:
    csv_file = csv.reader(csvfile)
    for data in csv_file:
        print(data)'''
