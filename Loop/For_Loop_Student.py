
d1 = {}

for i in range(1, 4):
    ID = int(input("ID "))
    d1[ID] = {}
    d1[ID]['Name'] = input("Name ")
    d1[ID]['Mark'] = {}
    d1[ID]['Mark']['M'] = int(input("Math Mark "))
    d1[ID]['Mark']['E'] = int(input("English Mark "))


print("Student Details - ", d1)

