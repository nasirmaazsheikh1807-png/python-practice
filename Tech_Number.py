print("Tech Number")
n = int(input("Enter a Number: "))
n = str(n)
length = len(n)
mid = len(n)//2
if len(n)%2 != 0:
    print(n,"The number is Not a Tech Number.")
else:
    l = n[:mid]
    r = n[mid:]
    sum = int(l)+int(r)
    if sum**2 == int(n): 
        print(n,"is a Tech Number.")
    else:
        print(n,"is not a Tech Number.")