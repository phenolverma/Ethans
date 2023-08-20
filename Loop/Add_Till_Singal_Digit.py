num = str(input("Please enter the digit you want to add = "))
num_list = list(num)
num_list_len = len(num_list)
flag = 1
while flag == 1:
    sum_num = 0
    if num_list_len >= 2:
        for each in num_list:

            sum_num = sum_num + int(each)
    num_list = list(str(sum_num))
    num_list_len = len(num_list)
    if num_list_len < 2:
        flag = 0
print(f"Sum of the digit  = {sum_num}")

