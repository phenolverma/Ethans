list1 = [11, 12, 14, 'Phenol', 11.1]
list_res = []
for each in list1:
    if type(each) == int:
        each = each ** 2
        list_res.append(each)
print(list_res)
