import csv

with open('data.csv', 'r',encoding='utf8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



