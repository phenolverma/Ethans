list_1 = [1, 2, 3, 4, 5]
list_2 = ['A', 'B', 'C', 'D', 'E']


def chk_dup(list_in):
    flag = 0
    list_set = set(list_in)
    if len(list_set) != len(list_in):
        flag = 1
    return flag


def Form_Dict(list_1_Input, list_2_Input):
    dict_created = {}
    for each in range(len(list_1_Input)):
        dict_created[list_1_Input[each]] = list_2_Input[each]
    return dict_created


if len(list_1) != len(list_2):
    print(f"Both list are not same length, can't create dictonary")
elif chk_dup(list_1) == 1 or chk_dup(list_2) == 1:
    print(f"List have same values, can't create dictonary")
else:
    print(Form_Dict(list_1, list_2))

print(dict(zip(list_1, list_2)))







