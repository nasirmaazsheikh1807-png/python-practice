print("Invalid Integer Input")
try:
    n = int(input("Enter A Number: "))
    print("You Entered: ", n)
except ValueError:
    print("Inalid Input! Please Enter A Number.")