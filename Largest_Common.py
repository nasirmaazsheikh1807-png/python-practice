print("Find The Largest Common Element")
a = {2,5,8,12,20}
b = {1,8,10,12,15}
common = set()
largest = 0
for i in a:
    for j in b:
        if i == j:
            common.add(i)
for i in common:
    if i > largest:
        largest = i
print(largest)