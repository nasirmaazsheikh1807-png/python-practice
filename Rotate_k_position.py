print("Rotate Tuple By K Positions")
n = (1,2,3,4,5,6)
k = 14
k = k % len(n)
r = len(n) - k
new = ()
for i in n:
    new = n[r:]
else:
    new += n[:r]
print(new)
