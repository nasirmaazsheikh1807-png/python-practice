print("Prime Number Checker")

x = int(input("Enter a number: "))

if x <= 1:
    print(x, "is not a prime number")
else:
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            print(x, "is not a prime number")
            break
    else:
        print(x, "is a prime number")