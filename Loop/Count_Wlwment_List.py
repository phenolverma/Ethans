list1 = [1, 7, 2, 2, 3, 4, 7, 2, 'Ethans', 1, 3, 5, 7, 3, 9, 'Ethans']
res = {}
for each in set(list1):
    count_char = list1.count(each)
    res[each] = count_char
print(res)
