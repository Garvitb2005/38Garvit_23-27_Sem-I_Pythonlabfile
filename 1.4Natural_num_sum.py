# 1.4 Write a program to print first n natural number & their sum
n = int(input("Enter a no upto which you want natural numbers printed "))
sum = 0
for i in range(1,n+1):
    sum+=i
    print(i)
print("Sum of",n,"natural numbers is",sum)
