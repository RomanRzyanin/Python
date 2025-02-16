import json

__all__ = ['save_to_json']


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_f:
        json.dump(data, json_f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    save_to_json()
