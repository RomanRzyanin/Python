def main(x):
    d = {}
    def loc(y):
        for i in range(y):
            d[i] = x ** i
        return d
    return loc

small = main(42)
big = main(73)
print(small(7), big(7), small(3), sep='\n')
print(main(55)(
    9))