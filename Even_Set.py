print("Even Numeber in Set")
a = {1,2,3,4,5}
b = {4,5,6,7}
even = set()
for i in a:
    for j in b:
        if i % 2 == 0:
            even.add(i)
        if j % 2 == 0:
            even.add(j)
print(even)