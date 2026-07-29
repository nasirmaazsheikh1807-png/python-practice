print("Most Frequent Element")
n = (2,4,2,5,4,2,7,4,2)
freq = ()
element = ()
for i in n:
    count = 0
    for j in n:
        if i == j:
            count += 1
    if i not in element:
        freq += count,
        element += i,
num = element[0]
highest = freq[0]
for i , j in enumerate(freq):
    if j > highest:
        highest = j
        num = element[i]
print(highest , num)







    
