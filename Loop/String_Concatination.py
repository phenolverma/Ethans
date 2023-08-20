list_to_con = [('G', 'E', 'E', 'K', 'S'), ('G', 'E', 'E', 'K', 'S'), ('G', 'E', 'E', 'K', 'SKKKKK')]
final_str = ''
for stri in list_to_con:
    for each in stri:
        final_str = final_str + each
print(final_str)