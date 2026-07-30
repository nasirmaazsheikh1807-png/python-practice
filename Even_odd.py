print("Split Even And Odd Element")
n = (12,7,5,8,10,3,6,9)
even = ()
odd = ()
for i in n:
    if i % 2 == 0:
        even += i,
    else:
        odd += i,

print(even)
print(odd)