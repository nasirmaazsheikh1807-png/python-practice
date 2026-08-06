print("Are Two Dictionaries Equal")
d1 = {
    "a":1,
    "b":2,
    "c":3
}
d2 = {
    "b":5,
    "a":1,
    "c":3
}
equal = True
for key ,value in d1.items():
    if key in d2:
        if d1[key] == d2[key]:
            equal = True
        else:
            equal = False
            break
if equal:
    print("Equal")
else:
    print("Not Equal")
