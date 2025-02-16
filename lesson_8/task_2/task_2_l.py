import json

def fun_dump_json():
    name = 'Петя'
    user_id = '002'
    level = 4

    with open('task8_2.json', 'r', encoding='utf-8') as f:
        res = json.load(f)
        print(res)

    my_dict = {
        'level': level,
        'id': user_id,
        'name': name,
    }

    with open('task8_2.json', 'w', encoding='utf-8') as js_f:
        res.append(my_dict)
        json.dump(res, js_f, indent=2, separators=(',', ':'), ensure_ascii=False)


lst = []
with open('task8_2.json', 'w', encoding='utf-8') as js_f:
    json.dump(lst, js_f)

s = 'n'
fun_dump_json()
