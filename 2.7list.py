# 2.7 Write a program for various list slicing operation.
# a= [10,20,30,40,50,60,70,80,90,100]
# i. Print Complete list
# ii. Print 4th element of list
# iii. Print list from0th to 4th index.
# iv. Print list -7th to 3rd element
# v. Appending an element to list.
# vi. Sorting the element of list.re
# vii. Popping an element.
# viii. Removing Specified element.
# ix. Entering an element at specified index.
# x. Counting the occurrence of a specified element.
# xi. Extending list.
# xii. Reversing the list.

a = [10,20,30,40,50,60,70,80,90,100]
print(a)                                 #i
print(a[3])                              #ii
print(a[:4])                             #iii
print(a[-7:4])                           #------iv
a.append(55)                             #V
print(a)
a.sort()                                 #Vi
print(a)                                 
a.pop(5)                                 #Vii           
print(a)
a.remove(60)                             #Viii
print(a)
a.insert(5,60)                           #iX
print(a)
print(a.count(20))                       #X
b = [110,120,130,140]
a.extend(b)                              #Xi
print(a)
a.reverse()                              #Xii
print(a)


