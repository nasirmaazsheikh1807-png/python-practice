print("Common Elements Cube")
a = {1,2,3,4,5}
b = {3,4,5,6,7}
common = set()
for i in a:
    for j in b:
        if i == j:
            common.add(i**3)
print(common)
