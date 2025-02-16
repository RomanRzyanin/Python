import json

#
# json_text = '''{
# "0" : "H",
# "1" : "e",
# "2" : "l",
# "3" : "l",
# "4" : "o",
# "5" : ",",
# "6" : " ",
# "7" : "w",
# "8" : "o",
# "9" : "r",
# "10" : "l",
# "11" : "d"
# }'''
# with open('new_json.json', 'r', encoding='utf-8') as f:
#     json_file = json.load(f)
# print(json_file)
# print(type(json_file))
# for el in json_file.values():
#     print(el, end='')
# print()
#
# json_list = json.loads(json_text)
# print(json_list)
# for el in json_list.values():
#     print(el, end='')
# print()
#
# json_my_text = json.dumps(json_file)
# print(json_my_text)
# print(type(json_my_text))
# for el in json_my_text:
#     if el.isalpha():
#         print(el, end='')
# print()
# print(2247 * 0.22)

a = 'Hello world!'
b = {key: value for key, value in enumerate(a, start=1)}

c = json.dumps(b, indent=3, separators=('; ', '= '))
print(c)
