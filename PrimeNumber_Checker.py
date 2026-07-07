print("Prime Number Checker")
x = int(input("Enter a number: "))
print("You entered:", x)
if x > 1:
    for i in range(2,x):
        if (x % i) == 0:
            print(x, "is not a prime number")
            break
        else:
            print(x, "is a prime number")
            break