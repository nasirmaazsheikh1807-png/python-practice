print("Invert A Dictionary")
n = {
    "a":1,
    "b":2,
    "c":3
}
d = {}
for key,value in n.items():
    d[value] = key
print(d)

