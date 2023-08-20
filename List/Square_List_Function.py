list_in = [2, 3, 4, 5, 6, 7, 8, 9]


def list_sqr(in_list):
    list_out = []
    for each in in_list:
        each = each ** 2
        list_out.append(each)
    return list_out


print(list_sqr(list_in))

