print("Remove Extra Spaces From String")
n = str(input("Enter A String: "))
new = ("")
prev = new[-1]
space = (" ")
for i in n:
    if i != "":
        new += i
    if prev != space:
        new += prev
    elif prev == space:
        prev = i

print(new)
