print("Disarium Number")
n = int(input("Enter a Number:"))
original = n
sum = 0
expo = 0
n = str(n)
for i , c in enumerate(n):
    expo = int(c)**(i+1)
    sum += expo
if sum == original:
    print(n, "is a Disarium number.")
else:
    print(n, "is not a Disarium Number.")

