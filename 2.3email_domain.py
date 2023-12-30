# Write a program that scans the email address and forms a tuple of username
# and domain.
n = 1
for i in range (0,n):
    mail = input("Enter your gmail ")
dom=()
user=()
for i in range(0,len(mail)):
    if(mail[i]=='@'):
        dom = mail[i:]
        username = mail[:i]
        i+=1
print("username:-",username)
print("domain:-",dom)