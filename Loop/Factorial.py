num = int(input("Enter the number = "))

def factorial(digit):
    fact = 1
    while digit > 0:
        fact = fact * digit
        digit -= 1
    return fact


for each in range(num):
    print(f"Factorial of {each} = {factorial(each)}")

