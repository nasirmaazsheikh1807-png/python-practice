print("Check If Two Sets Have Exatly one Common Element")
a = {1,2,3,4}
b = {4,5,6,7}
common = ()
for i in a:
    for j in b:
        if i == j:
            common += i,
if len(common) == 1:
    print("Sets Have Exactly One Common Element")
else:
    print("Sets Have Don't Have Exactly One Common Element")

