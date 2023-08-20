string = input("Enter a sting = ")
# while True:
#     new_string = 0
while string != string[::-1]:
    print(string, "->")
    string = int(string) + sum([int(each) for each in string])
else:
    print(string)

