import csv

__all__ = ['save_to_csv']


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csv_f:
        writer = csv.DictWriter(csv_f, fieldnames=['name', 'path', 'type', 'size', 'parent'])
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    save_to_csv()
