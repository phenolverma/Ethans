student_data = {}
ID = 100
add_more = True
del_more = True
ser_mor = True

while True:
    print('''
    Please select the option below,
    1- Add new student data
    2- Remove student data 
    3- Search student data
    4- Show the student details
    5- Exit''')
    option = input("Enter the option here -> ")
    if option == '1':  # Condition to add details for student
        add_more = True
        while add_more:
            student = {}
            student['Name'] = {}
            student['Name'] = input("Enter Student Name = ")
            student['Mark'] = {}
            student['Mark']['M'] = input("Enter Math Marks = ")
            student['Mark']['E'] = input("Enter English Marks = ")
            student_data[ID] = student
            ID += 1
            add_more_data = input("Do you want to add more student details - Y/N ")
            if add_more_data.upper() == 'N':
                add_more = False
        else:
            print(student_data)

    if option == '2':
        while del_more:
            del_more = True
            rem_ID = int(input("Enter the ID of the student to remove = "))
            if rem_ID in student_data:
                del student_data[rem_ID]
                del_more_data = input("Do you want to delete more student details - Y/N ")
                if del_more_data.upper() == 'N':
                    del_more = False
            else:
                print("No data to delete, please add the data")
                del_more = False

    if option == '3':
        while ser_mor:
            ser_mor = True
            ser_data = int(input("Enter the ID to search the details = "))
            if ser_data in student_data:
                print(student_data[ser_data])
                ser_mor_data = input("Do you want to search more student details - Y/N ")
                if ser_mor_data.upper() == 'N':
                    ser_mor = False
            else:
                print("Data not present, please try adding data")
                ser_mor = False

    if option == '4':
        if student_data == {}:
            print("Not student data is available to show")
        else:
            print(student_data)

    if option == '5':  # Condition to exit from details of the student
        print("Thank you, please visit again!")
        break
