import csv,json
from json import *
json = {}
with open('data.csv') as csv_file:
    data = csv.DictReader(csv_file)
    for rows in data:
        field = rows['cdatetime']
        json[field] = rows
print(json)

with open ('data.json','w') as jsonfile:
    jsonfile.write(json.dump(json,indent = 4))
    