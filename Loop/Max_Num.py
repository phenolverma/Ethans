list_max = [1, 3, 5, 3, 70, 4, 5, 6]


def max_num(list_pass):
    max_num1 = list_pass[0]
    for num in list_pass:
        if max_num1 < num:
            max_num1 = num
    return max_num1


print(f" {max_num(list_max)} is the maximum number in the provided list")

