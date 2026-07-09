print("Reverse a Number")
n = int(input("Enter a number: "))
r = 0
rev = 0
while n > 0:
    r = n%10
    n //= 10
    rev = rev*10+r
print(rev)
