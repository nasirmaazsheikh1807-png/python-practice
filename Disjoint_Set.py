print("Check If Sets Are Disjoint or Not")
a = {1,2,3}
b = {4,5,6}
condition = False
for i in a:
    for j in b:
        if i == j:
            condition = True
            break
if condition:
    print("Sets Are Not Disjoint")
else:
    print("Sets Are Disjoint")