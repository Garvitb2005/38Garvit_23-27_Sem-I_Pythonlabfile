# 4.3 Write a program to admit the students in the different
# Departments(pgdm/btech)and count the students. (Class, Object and Constructor).
#Admisison process...............
class ITM:
    
    def __init__(self):
        self.name = input("Enter your name ")
        self.age = int(input("Enter your age "))
        self.department =int((input("Which department you want in\n1.Pgdm\n""2.Btech\n ")))
        
        
    def display(self):
        if self.department == 1:
            print("*****Btech Department*****")
            print("Name:-",self.name)
            print("Age:-",self.age)
           # print("Department:-",self.department)
        elif self.department == 2:
            print("*****Pgdm Department*****")
            print("Name:-",self.name)
            print("Age:-",self.age)
          #  print("Department:-",self.department)

list = []
n = int(input("How many students data you are entrying "))
for i in range(n):
    student = ITM()
    list.append(student)
for student in list:
    student.display()

