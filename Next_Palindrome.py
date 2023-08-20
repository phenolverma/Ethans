def next_palindrome(num):
    while str(num) != str(num)[::-1]:
        num = num + 1
    else:
        return num


num_enter = input("Enter the number to check = ")
print(f"Next palindrome number to the given number {num_enter} is {next_palindrome(int(num_enter))}")

print([])

