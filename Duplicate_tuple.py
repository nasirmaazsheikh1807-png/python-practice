print("Remove Duplicates From Tuples")
n = (1,2,3,2,4,1,5,3)
uniq = ()
for i in n:
    if i not in uniq:
        uniq += (i,)
print(uniq)