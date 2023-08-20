class Student:
    def __init__(self, groll, gname):
        self.roll = groll
        self.name = gname

    def disp(self):
        print('Name', self.name)
        print('Roll', self.roll)


s1 = Student(101, 'Mayank')
s2 = Student(102, 'Jatin')
s1.disp()
