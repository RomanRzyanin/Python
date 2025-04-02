with open('files.txt', 'r', encoding='utf-8') as f:
    data_dict = {}
    for line in f:
        data = f.readline().strip('\n').split()
        # print(data)
        if data:
            name = data[0]
        # data.insert(0, name.split('.')[0])
        data_dict.setdefault(name.split('.')[1], []).append(data)
        # data_dict[name.split('.')[1]] = data

        # print(data)
for k, v in data_dict.items():
    for el in v:
        print(el[0], sep='\n')
