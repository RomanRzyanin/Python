import csv

def read_csv(file):
    with open(file, 'r', newline='', encoding='utf-8') as f:
        data = list(csv.reader(f))
    return data