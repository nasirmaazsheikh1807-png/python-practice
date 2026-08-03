print("Duplicate Characters")
n = input("Enter A String: ")
freq = {}
duplicate = ()
for i in n:
    if "a" <= i <= "z":
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
for ch in n:
    if freq[ch] > 1:
        if ch not in duplicate:
            duplicate += ch,
print(duplicate)