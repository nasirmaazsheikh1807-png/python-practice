print("Symmetric Difference")
a = {1,2,3,4,5}
b = {4,5,6,7}
n = set()
for i in a:
    for j in b:
        if i in b:
            continue
        else:
            n.add(i)
        if j in a:
            continue
        else:
            n.add(j)
print("Symmetric Difference:" , n)