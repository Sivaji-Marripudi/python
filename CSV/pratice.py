'''import csv,json
from json import *
json = {}
with open('data.csv') as csv_file:
    data = csv.DictReader(csv_file)
    for rows in data:
        field = rows['cdatetime']
        json[field] = rows
print(json)'''
'''
import csv
rows = []
filed_names = []
with open('data.csv','r') as f:
    data = csv.reader(f)
    filed = next(data)
    for i in data:
        print(i)
print('rows are ',data.line_num)
print(filed)'''


