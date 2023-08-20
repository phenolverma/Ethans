count_str, count_hash = 1, 9
while count_str < 10:
    print('^' * count_str, '#' * count_hash)
    count_hash -=1
    count_str += 1

