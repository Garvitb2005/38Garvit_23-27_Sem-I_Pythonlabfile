n = int(input("Enter a number to check if its perfect or not"))
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum+=i
if sum == n:
    print("It is a perfect number")
else:
    print("Its not a perfect number")
    
    