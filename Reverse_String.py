print("Reverse a String")
n = str(input("Enter a String: "))
i = len(n)-1
rev = ("")
while i >= 0:
    rev += n[i]
    i -= 1

print(rev)


