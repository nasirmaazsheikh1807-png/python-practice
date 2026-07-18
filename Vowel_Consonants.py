print("Count Vowel And Consonants")
S = str(input("Enter a String: ")).lower()
v = 0
c = 0
for i in S:
    if i in "a,e,i,o,u":
        v += 1
    else:
        c += 1

print("Vowels:" , v)
print("Consonants:", c)