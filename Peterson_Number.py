print("Peterson Number Checker Program")
n = int(input("Enter a Number: "))
original = n
sum = 0
def fact(a):
    if a == 0 or a == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, a + 1):
            factorial *= i
    return factorial

n = str(n)
for i in n:
    sum += fact(int(i))
if sum == original:
    print(n, "is a Peterson Number.")
else:
    print(n, "is not a Peterson Number.")