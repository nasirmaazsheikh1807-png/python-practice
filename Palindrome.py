print("Welcome To Pallindrome Checker")
x = int(input("Enter a number to check if it is a palindrome or not: "))
if str(x) == str(x)[::-1]:
    print(f"The given number {x} is a palindrome")
else:
    print(f"The given number {x} is not a palindrome")
