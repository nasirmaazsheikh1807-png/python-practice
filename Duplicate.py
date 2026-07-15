print("Duplicate Numbers")
n = [1,2,2,3,4,4,5,5,5]
printed = []
for i in n:
    count = 0
    for j in n:
        if i == j:
            count += 1
    if count > 1 and i not in printed:
        print(i)
        printed.append(i)



