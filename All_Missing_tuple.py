print("Find All Missing Numbers In The Given Tuple")
n = tuple(map(int,input("Enter a Tuple: ").split()))
missing = ()
previous = n[0]
for i in n[1:]:
    while previous +1 != i:
            missing += (previous +1,)
            previous += 1
    previous = i
print(n , missing)