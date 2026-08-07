print("Count Common Elements")
a = {1,2,3,4,5}
b = {3,4,5,6,7}
count = 0
for i in a:
    for j in b:
        if i == j:
            count += 1
print("Common Elements:" , count) 