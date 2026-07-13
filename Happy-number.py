print("Happy Number")
n = int(input("Enter a Number: "))
original = n
while n != 1 and n != 4:
    sum = 0
    for digit in str(n):
        digit = int(digit)
        digit *= digit
        sum += digit
        n = sum
    if n == 1:
        print(original,"is a Happy Number.")
        break
else:
    print(original,"is not a Happy Number.")
    