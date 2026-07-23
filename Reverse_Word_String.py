print("Reverse Every Word in a String")
n = str(input("Enter A String: "))
rev = ("")
word = ("")
for i in n:
    if i != " ":
        word += i
    elif i == " ":
        j = len(word)-1
        while j >=0:
            rev += word[j]
            j -= 1
        rev += " "
        word = ""
j = len(word)-1
while j >= 0:
    rev += word[j]
    j -= 1
print(rev)