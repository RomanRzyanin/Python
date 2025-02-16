__all__ = ['edit_data']


def edit_data(data):
    for i in range(len(data)):
        if i == 0:
            data[i].append('revenue')
        else:
            revenue = round(int(data[i][1]) * float(data[i][2]), 2)
            data[i].append(str(revenue))
    return data
