print("Armstrong Number")
n = int(input("Enter a number: "))
n = str(n)
length = len(n)
sum = 0
for i in n:
    sum += int(i)**length
if sum == int(n):
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")