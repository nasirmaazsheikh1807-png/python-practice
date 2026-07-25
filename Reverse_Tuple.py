print("Reverse The Tuple")
n = (1,2,3,4,5)
rev = ()
i = len(n) - 1
while i >= 0:
    rev += n[i],
    i -= 1
print(rev)