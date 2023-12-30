# Write a program to take input from user for addition of two numbers using
# (single inheritance).

class Parent:
    def add(self,a,b):
         return a+b

class child(Parent):                #deriving from base class
    def takevalue(self):
        a = int(input("Enter value of a "))
        b = int(input("Enter value of b "))
        print("addition is",self.add(a,b))
obj=child()
obj.takevalue()