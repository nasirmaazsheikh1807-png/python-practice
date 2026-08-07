print("If Common Exists in Given Sets")
a = {1,2,3,4,5}
b = {3,4,5,6,7}
common = True
for i in a:
    for j in b:
        if i == j:
            common = True
            break
        else:
            common = False
if common:
    print("Common Elements Exists")
else:
    print("Common Elements Don't Exists")
            