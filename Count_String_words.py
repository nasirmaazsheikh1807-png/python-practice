print("Count Words in a String")
n = str(input("Enter a String: "))
count = 0
for i in n:
    if i == (" "):
        count += 1
Words = count + 1
print(Words)