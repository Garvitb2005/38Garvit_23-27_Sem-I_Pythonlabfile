#wap that defines the list of contrys that are member of Brics
lst=["BRAZIL","RUSSIA","INDIA","CHINA","SRI LANKA"]

choice = input("Enter the contry you want to know : ")

if choice.upper() in lst:
    print("In")
else:
    print("out")