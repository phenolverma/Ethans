from itertools import groupby
list_inp = [1, 2, 2, 3, 5, 4, 6, 6, 6, 2, 2, 8, 8]

res = [i[0] for i in groupby(list_inp)]

print(res)

