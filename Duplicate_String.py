print("Remove Duplicates From a String")
n = str(input("Enter a String: "))
unique = ("")
for i in n:
    count = 0
    for j in n:
        if i == j:
            count += 1
    if i not in unique:
        unique += i
print(unique)
