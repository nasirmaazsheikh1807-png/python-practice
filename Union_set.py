print("Unioun Of Two Sets")
a = {1,2,3,4,5}
b = {4,5,6,7}
c = set()
for i in a:
    c.add(i)
for i in b:
    c.add(i)
print(c)