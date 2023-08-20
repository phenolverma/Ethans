dic = {'fName':'Phenol','lName':'Verma','Age':42}
user_key = input("Enter the key = ")
if user_key in dic.keys():
    print(user_key, "is present in dictionary as a key and the value of key is",dic[user_key])
else:
    print(user_key, "key is not present in dictionary")