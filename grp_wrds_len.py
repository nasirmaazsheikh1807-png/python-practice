print("Group By Words By Length")
n = input("Enter A String: ").lower()
n = n.split()
word = {}
new = []
for i in n:
    if "a"<= i <= "z":
        if len(i) in word:
            word[len(i)].append(i)
        else:
            word[len(i)] = []
            word[len(i)].append(i)
print(word)