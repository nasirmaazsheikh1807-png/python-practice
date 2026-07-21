print("Convert Uppercase To Lowercase")
n = str(input("Enter a String: "))
Case = ""
i = len(n)
for i in n:
    if "A" <= i <= "Z":
        n = (i).lower()
        Case += n
    elif "a" <= i <= "z":
        n = (i).upper()
        Case += n
    else:
        n = i 
        Case += n

print(Case)