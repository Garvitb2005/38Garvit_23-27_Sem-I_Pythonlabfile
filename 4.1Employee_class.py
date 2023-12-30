# 4.1 Write a program to Create Employee Class & add methods to get employee
# details & print.
import random
class Employee:
    def getdetails(self):
        self.id = random.randint(0,100)
        self.name = input("Enter your name ")
        self.salary = 50000
        self.department = input("Enter your department ") 
    def display(self):
        print("ID :-",self.id)
        print("Name :-",self.name)
        print("Department :-",self.department)
list = []
n = int(input("How many Employee data you are entrying "))
for i in range(n):
    Emp = Employee()
    Emp.getdetails()
    list.append(Emp)
for student in list:
    Emp.display()



