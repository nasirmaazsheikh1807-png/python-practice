print("Harshad Number")
n = int(input("Enter a Number: "))
original = n 
n = str(n)
sum = 0
for i in n:
    sum += int(i)
if original % sum == 0:
    print(n , "is a Harshad Number.")
else:
    print(n , "is not a Harshad Number.")