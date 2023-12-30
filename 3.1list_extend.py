# 3.1 Write a program to extend a list in python by using given approach.
# i. By using + operator.
# ii. By using Append ()
# iii. By using extend ()

a = [10,20,30,55,60,50,80]
b = [90,110,120,25]
print(a+b)              #i
a.append(b)
print(a)                #ii
a.extend(b)
print(a)                #iii