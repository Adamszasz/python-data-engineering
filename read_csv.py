import csv


with open('python-data-engineering/data_files/data.csv') as f:
    myreader = csv.DictReader(f)
    headers = next(myreader)
    for row in myreader:
        print(row['name'])
