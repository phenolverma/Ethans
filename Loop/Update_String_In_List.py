orl_str = input("Enter the string to be added before each list item = ")
orl_list = [1, 2, 3, 4]
upt_list = []
for val in orl_list:
    upt_list.append(orl_str + str(val))
print(upt_list)
