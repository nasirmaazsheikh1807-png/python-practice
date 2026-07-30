print("Consecutive Duplicate remove")
n = (1,1,2,2,2,3,1,1,4,4,5)
new = n[0],
for i in n:
    if new[-1] != i:
        new += i,
    else:
        if new != i and new[-1] != i:
            new += i,

print(new)