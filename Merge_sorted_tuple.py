print("Merge Two Sorted Tuples")
a = (1,3,5,7,9)
b = (2,4,6,8,10)
new = ()
i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        new += a[i],
        i += 1
    elif a[i] > b[j]:
        new += b[j],
        j += 1
print(new)