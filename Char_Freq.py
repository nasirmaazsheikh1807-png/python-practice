print("Character Frequency")
n = input("Enter a  String: ").lower()
freq = {}
for i in n:
    if "a" <= i <= "z":
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
print(freq)