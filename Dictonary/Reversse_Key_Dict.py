dict_to_rev = {1: 'A', 2: 'B', 3: 'C'}
print(f"Original dictionary is {dict_to_rev}")
reversed_dict = {}
for key in dict_to_rev:
    val = dict_to_rev[key]
    reversed_dict[val] = key
print(f"Reversed dictionary is {reversed_dict}")
