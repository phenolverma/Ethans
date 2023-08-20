num1, num2 = 0, 1
count = 0
len_fib = int(input("Please enter the lenght = "))
while count < len_fib:
    print(num1)
    next_num = num1 + num2
    # update values
    num1 = num2
    num2 = next_num
    count += 1
