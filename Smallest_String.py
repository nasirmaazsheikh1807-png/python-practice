print("Smallest Word of The String")
n = str(input("Enter a String: "))
smallest = ("")
word = ("")
for i in n:
    if i != (" "):
        word += i

    if i == (" "):
        if smallest == (""):
            smallest = word
        if len(word) < len(smallest):
            smallest = word
        else:
            word = ("")
print(smallest)