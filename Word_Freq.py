print("Word Frequency Counter")
n = input("Enter a String: ").lower()
n = n.split()
word = {}
for i in n:
    if "a" <= i <= "z":
        if i in word:
            word[i] += 1
        else:
            word[i] = 1
print(word)
