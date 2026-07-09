print("Identifying Strong Number")
n = int(input("Enter a Number: "))
total = 0
temp = n
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(2, digit+1):
        if digit == 1 or digit == 0:
            fact = 1;
        else:
            fact *= i
    total = total + fact
    temp //= 10
if total == n:
    print(n, "is a Strong Number")
else:
    print(n, "is not a Strong NUmber")



    