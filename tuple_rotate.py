print("Tuple Rotation By Right One Position")
n = (10,20,30,40,50)
num = (n[-1])
new = (n[-1],)
for i in n:
    if i == num:
        continue

    new += i,
print(new)