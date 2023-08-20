str1 = str(input("Please enter the string = "))
temp = str1
list1 = []
for i in range(len(str1)):
    temp = temp[1:] + temp[0]
    list1.append(temp)
print(list1)

