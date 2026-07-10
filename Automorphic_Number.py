print("Automorphic Number")
n = int(input("Enter a Number: "))
original = n
sq = n*n
n = str(n)
length = len(n)
auto = sq % 10**length
if auto == original:
    print(n , "Is an Automorphic Number")
else:
    print(n ,"Is not an Automorphic Number")    