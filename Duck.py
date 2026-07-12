print("Duck Number Checker Program")
n = int(input("Enter a Number: "))
n = str(n)
if n[0] != "0" and  "0" in n[1:]:
    print(n, "is a Duck Number")
else:
    print(n, " is not a Duck Number")