num = int(input("Enter a num - "))

try:
    l1 = [1, 2, 3, 4, 5]
    print(1/num)
except Exception as e:
    print(e)
    print(l1[4])
else:
    print("No exception")

finally:
    print("Clean process")
