print("Remove Duplicates")
n = [1,2,2,3,4,4,5,1]
unique = []
for i in n:
    if i not in unique:
        unique.append(i)
print(unique)

