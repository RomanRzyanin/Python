import sys

import random as r

print(11_000_000 / 100)
# print(*sys.path, sep='\n')

print(r.uniform(10, 1010))
print(r.randrange(10, 1010, 10))
print(r.sample(range(10, 1010, 10), 10))
print(r.sample([1, 2], 5, counts=[1, 23]))
