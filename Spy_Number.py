print("Spy Number")
n = int(input("Enter a Number: "))
original = n
sum = 0
product = 1
n = str(n)
for i in n:
    sum += int(i)
    product *= int(i)
if sum == product:
    print(n, "is a Spy Number.")
else:
    print(n, "is not a Spy Number.")