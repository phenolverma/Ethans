str1 = str(input("Enter first string = ")).upper()
str2 = str(input("Enter second string = ")).upper()
str1_list = list(str1)
str2_list = list(str2)

str1_list.sort()
str2_list.sort()

if str1_list == str2_list:
    print("Anagram")
else:
    print("Not Anagram")

