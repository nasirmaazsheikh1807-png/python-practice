print("Basic Set Operations")
a = {1,2,3,4,5}
b = {4,5,6,7,8}
common = set()
only_a = set()
only_b = set()
for i in a:
    for j in b:
        if i == j:
            common.add(i)
        if i in b:
            continue
        else:
            only_a.add(i)
        if j in a:
            continue
        else:
            only_b.add(j)
print(common,only_a,only_b,end=" ")