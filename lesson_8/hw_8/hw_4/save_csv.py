import csv

__all__ = ['save_csv']


def save_csv(data, file):
    with open(file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

