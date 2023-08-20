low_prime = int(input("Enter the lower limit of prime number = "))
upr_prime = int(input("Enter the upper limit of prime number = "))
count = 0
for num in range(low_prime, upr_prime):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            count += 1
            print(num)
print(f"Total Prime Number between {low_prime} and {upr_prime} is {count} ")


