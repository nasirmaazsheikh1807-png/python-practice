print("Pallindrome String Checker")
n = str(input("Enter a String: ")).lower()
i = len(n)-1
rev = ("")
while i >= 0:
    rev += n[i]
    i -= 1
if n == rev:
    print(n, "is a Pallindrome String.")
else:
    print(n,"is not a Pallindrome String.")


