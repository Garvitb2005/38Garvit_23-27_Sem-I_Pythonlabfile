# Write a Python function that accepts a string and counts the number of upper-
# and lower-case letters.

# string_test= 'Today is My Best Day'
a=input("Enter a string: ")
ucount=0
lcount=0
for i in a:
    if i.islower():
        lcount+=1
    elif i.isupper():
        ucount+=1
print(a)
print("Number of lower case letters:",lcount)
print("Number of upper case letters:",ucount)