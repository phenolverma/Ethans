orgnl_str = input("Enter the statement string = ")
word_len_to_conv = int(input("Please enter the length of the word to convert = "))
caps_str1 = orgnl_str.upper()
my_list = list(caps_str1.split())
valu = ''
count = 0
final_list = []
com_list = []
for word in my_list:
    len_word = len(word)
    char_word = list(word)
    if len_word == word_len_to_conv:
        count += 1
        final_list.clear()
        valu = ''
        for each in word:
            valu = valu + each
            final_list.append(valu)
        print(f"Occurrence {count}, {word_len_to_conv} character word {final_list}")

if com_list == final_list:
    print(f"No occurrence of {word_len_to_conv} character word in the statement provided.")


