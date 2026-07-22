print("Remove Extra Spaces From String")
n = str(input("Enter A String: "))
new = ("")
for i in n:
    if i != " ":
        new += i
    else:
        if new != "" and new[-1] != " ":
            new += " "
if new != "" and new[-1] == " ":
    new = new[:-1]

print(new)
