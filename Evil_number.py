print("Evil Number Detector")
n = int(input("Enter a Number: "))
original = n
n = bin(n)
sum = 0
for i in n:
    if n == 1:
        sum += i
if sum % 2==0:
    print(n , "is a Evil Number.")
else:
    print(n, "is not a Evil Number.")
