print("Merge Two Dictionaries")
d1 = {
    "a": 10,
    "b": 20
}
d2 = {
    "c": 30,
    "d": 40
}
new = {}
for i,j in d1.items():
    new[i] = j
for i, j in d2.items():
    new[i] = j
print(new)