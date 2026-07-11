print("Neon Numbers")
n = int(input("Enter a Number: "))
original = n
sq = n*n
sq = str(sq)
sum = 0
for i in sq:
    sum += int(i)
if sum == original:
    print(n , "is a Neon Number")
else:
    print(n , "is not a Neon Number")
