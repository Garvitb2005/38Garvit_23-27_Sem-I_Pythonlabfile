# Write a program that creates dictionary of cube of odd numbers in the range.
n = int(input("Enter any number"))
d={}
for i in range(1,n):
    if(i%2!=0):
        d[i] = i*i*i
print(d)