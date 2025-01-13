# task_2
#
e, n = 3, 10
i = 1
res = 0
while i <= n:
    if i % e != 0 and i % 2 == 0:
        res += i
    i += 1
print(res)
