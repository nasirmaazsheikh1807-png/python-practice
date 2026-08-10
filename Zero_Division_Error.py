print("Handling Zero Division Error")
a = float(input("Enter The First Number: "))
b = float(input("Enter Your Second Number: "))
try:
    print(a/b)
except  ZeroDivisionError:
    print("Not Possible Bruder")