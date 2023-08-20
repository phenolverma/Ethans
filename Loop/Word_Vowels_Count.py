orgnl_str = input("Enter the statement string = ")
caps_str1 = orgnl_str.upper()
print(f"Words in statement = {len(caps_str1.split())}")
my_list = list(caps_str1.split())
count = 0
for word_list in my_list:
    for char_list in word_list:
        if 'A' in char_list:
            count += 1
        if 'E' in char_list:
            count += 1
        if 'I' in char_list:
            count += 1
        if 'O' in char_list:
            count += 1
        if 'U' in char_list:
            count += 1


print(f"Vowels in the given string is = {count}")


