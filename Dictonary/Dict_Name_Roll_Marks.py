dic = {}
roll_num = int(input("Enter the roll number = ")) # declaring roll number
dic[roll_num] = {} # passing roll number
name = input("Enter the name = ") # declaring name of the student
dic[roll_num]['Name'] = name # passing name
mEng = int(input("Enter English number = ")) # declaring mark of english
mMaths = int(input("Enter Maths number = ")) # declaring mark of math
dic[roll_num]['Marks'] = {}
dic[roll_num]['Marks']['English'] = mEng # passing mark of english
dic[roll_num]['Marks']['Maths'] = mMaths # passing mark of math
dic[roll_num]['Scholarship'] = {}
if mMaths >= 70:
    dic[roll_num]['Scholarship'] = 2000
elif mMaths >= 60 and mMaths < 70:
    dic[roll_num]['Scholarship'] = 1500
elif mMaths >= 40 and mMaths < 60:
    dic[roll_num]['Scholarship'] = 1000
else:
    dic[roll_num]['Scholarship'] = 0
print(dic)