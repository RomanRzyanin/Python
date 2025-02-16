import csv

__all__ = ['save_csv']


def save_csv(data, file):
    with open(file, 'w', encoding='utf-8', newline='', ) as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
