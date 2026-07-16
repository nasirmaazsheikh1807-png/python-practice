print("Finding Missing Number in List")
n = [1,2,3,4,6,7,8,9,10]
unique = []
for i in range(1,11):
    for j in n:
        if i not in n:
            unique.append(i)
            break

print(unique)            