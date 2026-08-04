print("Find All Non Repeating Characters")
n = input("Enter a String: ")
freq = {}
non = ()
for i in n:
    if "a" <= i <= "z":
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
for ch in n:
    if freq[ch] == 1:
        non += ch,
print(non)

