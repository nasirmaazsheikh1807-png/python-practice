print("Capitilize The First Letter Of every Word")
n = str(input("Enter A String: "))
new = ("")
for i in n:
    if i != "":
        if i == " ":
            new += i
        elif new == "":
            new += (i).upper()
        elif "a"<= i <="z" and new[-1] == " ":
            new += (i).upper()
        else:
            new += i

print(new)