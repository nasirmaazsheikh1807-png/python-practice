print("Move All Zeros To The End")
n = (0,5,0,3,8,0,2)
new = (0)
a = ()
count = 0
for i in n:
    if i == new:
        count += 1
        continue
    a += i,
while count > 0:
    a += new,
    count -= 1
print(a)
