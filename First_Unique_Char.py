print("First Unique Character")
n = input("Enter a  String: ").lower()
freq = {}
for i in n:
    if "a" <= i <= "z":
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
for ch in n:
    if freq[ch] == 1:
        print(ch)
        break