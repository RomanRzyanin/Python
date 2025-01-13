# task_5
steps = 5
fig = '*'
space = ' '
n_fig = 1
n_space = steps - 1
for _ in range(steps):
    print(space * (n_space), fig * n_fig, space * n_space, sep='')
    n_fig += 2
    n_space -= 1
