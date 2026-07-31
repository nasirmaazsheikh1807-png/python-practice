print("Longest Consecutive Streak")
n = (3,4,5,2,7,8,9,10,1,2)
longest = n[0],
current = n[0],
for i in n:
    if i > current[-1]:
        current += i,
    else:
        if i < current[-1]:
            if len(current) > len(longest):
                longest = current
                current = i,
if len(current) > len(longest):
    longest = current
print(longest,len(longest))
    
    
        
