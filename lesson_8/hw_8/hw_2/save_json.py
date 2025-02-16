import json

__all__ = ['save_json']


def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_f:
        json.dump(data, json_f, indent=4, ensure_ascii=False)