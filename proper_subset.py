print("Check Whether One Set is a proper Subset Of Another")
a = {1,2,3}
b = {1,2,3,4,5}
condition = True
count = 0 
if a in b:
    condition = True
else:
    condition = False
for i in b:
    count += 1
if count != len(a):
    condition = True
if condition:
    print("a is a proper subset of b")
else:
    print("a is not a proper subset of b")
