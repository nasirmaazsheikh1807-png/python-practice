print("Find Missing Number")
n = tuple(map(int,input("Enter Elements: ").split()))
missing = ()
previous = n[0],
for i in n:
    if i == previous[-1] +1:
        previous += i,
    elif i != previous[-1]+1:
        missing = previous[-1]+1
print(n)
print(missing)


    
