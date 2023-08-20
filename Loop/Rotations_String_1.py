str1 = str(input("Please enter the string = "))
str1_len = len(str1)
str1_list = list(str1)
char_str = 0


def rev_string(str1_list_arug):

    str1_sum = ''
    flag = 1
    list_indx = 0
    while list_indx < str1_len-1:
        if flag == 1:
            str_last = str1_list_arug[0]
        str1_list_arug[list_indx] = str1_list_arug[list_indx+1]
        str1_sum = str1_sum + str(str1_list_arug[list_indx])
        list_indx += 1
        flag = 0
        if list_indx == str1_len:
            flag = 1
    new_string = str1_sum + str_last
    return new_string


final_list = []
list_item_final_list = ''
var = rev_string(str1_list)
final_list.append(var)
val1 = ''

while char_str < str1_len-1:
    list_item_final_list = final_list[char_str]
    var1 = rev_string(list(list_item_final_list))
    final_list.append(var1)
    char_str += 1

print(final_list)






