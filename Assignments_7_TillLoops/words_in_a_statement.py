from collections import Counter
statmt = "My name is Phenol Verma and my  nick name is Rockey Verma"

count_word = Counter(statmt.split()).most_common()

print(count_word)

