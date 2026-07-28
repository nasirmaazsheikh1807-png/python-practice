print("Merge Two Tuples Without Duplicates")
a = (1,2,3,4,5)
b = (4,5,6,7,2)
c = a+b
merge = ()
for i in c:
    if i not in merge:
        merge += i,
print(merge)