print("Find Elements Present In Only One Tuple")
a = (1,2,3,4,5)
b = (3,4,5,6,7)
c = a+b
one = ()
for i in c:
    if i not in b:
        one += i,
    if i not in a:
        one += i,

print(one)
