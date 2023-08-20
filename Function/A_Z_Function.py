from functools import reduce
def conver_ascii(num):
    return chr(num)


print(list(map(conver_ascii, range(65, 91)))) # printing A-Z with the help of conver_ascii function
print(list(map(chr, range(65, 91)))) # return same number of values as passed in list
print(reduce(lambda a, b: a+b, [1, 2, 3, 4])) # return only 1 value
print(reduce(lambda a, b: a+b, range(1, 4))) # Factorial calculation
print(list(filter(lambda X: X > 7, range(1, 25)))) # filter out greater than 7
print(list(filter(lambda X: (X % 7 == 0), range(1, 101)))) # filter the values divided by 7
print([chr(x) for x in range(65, 91)]) # Comrehenssion
print([x**2 for x in range(1, 26)])
print([x**2 for x in range(1, 26) if x % 2 == 0])
print([x**2 if x % 2 == 0 else x**3 for x in range(1, 26)])
print({x:x**2 for x in range(1, 5)})
print({x:chr(x+64) for x in range(1, 27)})

dict_giv = {1: 2, 2: 3, 4: 5}
print({dict_giv[each]:each for each in dict_giv})

