list1 = [1, 2, 3, 4, 5, 6, 7]
each = 0
even_count = 0
odd_count = 0

for each in list1:
    if each % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count, odd_count)

