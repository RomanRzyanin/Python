import json
import csv

def json_to_csv():
    with open('task8_2.json', 'r', encoding='utf-8') as js_f:
        res = json.load(js_f)
        lst = []
        keys = res[0].keys()
        lst.append(keys)
        for el in res:
            vals = el.values()
            lst.append(vals)

    with open('task8_2.csv', 'w', newline='', encoding='utf-8') as cs_f:
        writer = csv.writer(cs_f)
        for el in lst:
            writer.writerow(el)
    #print(keys)


json_to_csv()