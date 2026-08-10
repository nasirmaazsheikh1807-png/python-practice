print("Division Handler With Number")
try: 
    a = float(input("Enter The First Number: "))
    b = float(input("Enter The Second Number: "))
    print(a/b)
except ValueError:
    print("Invalid Input! Please Enter A Valid Number.")
except ZeroDivisionError:
    print("You Entered Zero")