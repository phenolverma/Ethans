num = 1
while num <= 10:
    if num == 7:  # Skip 7
        num += 1
        continue
    if num == 9:  # Breaking at 9
        break
    square = num ** 2
    print(f"Square of {num} = {square}")
    num += 1
else:
    print("Success")  # This will print if only while loop get success
