string = input("Enter a sting = ")
if string == string[::-1]:
    print(string, "is a palindromes string")
else:
    print(string, "is not palindromes string")