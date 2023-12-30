# 1.7 Write a program using for loop to calculate factorial of a No.
n = int(input("Enter a number "))
fact =1
for i in range(1,n+1):
    fact = fact*i
print("factorial is",fact)