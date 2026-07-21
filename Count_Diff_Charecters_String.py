print("Count , Alphabets , Digits and Special Characters")
n = str(input("Enter a String: "))
letter = 0
digit = 0
special = 0
for i in n:
    if "a" <= i <= "z" or "A" <= i <= "Z":
        letter += 1
    elif "0" <= i <= "9":
        digit += 1
    else:
        special += 1

print(f"letter: {letter} , digit: {digit},special:  {special}")
        