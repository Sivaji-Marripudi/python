import csv
with open("data.csv","r") as csvfile:
    csv_file = csv.reader(csvfile)
    with open("new_data.csv","w") as new_csvfile:
        csv_writer = csv.writer(new_csvfile,delimiter = "-")
        for data in csv_file:
            csv_writer.writerow(data)
