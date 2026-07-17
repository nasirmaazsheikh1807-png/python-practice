print("Rotate List Left By One")
n = [10,20,30,40,50]
num = 10
new = []
for i in n:
    if i == num:
        continue
        
    new.append(i)
new.append(num)
print(new)

