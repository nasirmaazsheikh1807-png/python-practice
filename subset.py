print("Whether One Set Is a Subset Of Another")
a = {1,2,3}
b = {1,2,3,4,5}
condition = True
for i in a:
    if i not in b:
        condition = False
        break
if condition:
    print("a is subset of b")
else:
    print("a is not a subset of b")