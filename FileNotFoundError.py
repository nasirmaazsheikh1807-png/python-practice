print("FileNotFoundError")
try:
    n = input("Enter A Filename: ")
    with open(n ,"r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("You Entered A Wrong File Name! Please Enter A Valid File Name.")

