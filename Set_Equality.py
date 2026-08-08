print("If Sets Are Equal Or Not")
a = {1,2,3,4}
b = {4,3,2,5}
count = 0
for i in a:
    for j in b:
        if i == j:
            count += 1
if count == len(a):
    print("Sets Are Equal")
else:
    print("Sets Are Not Equal")