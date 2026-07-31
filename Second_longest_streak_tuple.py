print("Second Longest Increasing Streak")
n = (3,4,5,2,7,8,9,10,1,2,3,4)
current = n[0],
longest = n[0],
second_longest = n[0],
for i in n:
    if i > current[-1]:
        current += i,
    else:
        if i < current[-1]:
            if len(current) > len(longest):
                second_longest = longest
                longest = current
            elif len(current) > len(second_longest) and len(current) != len(longest):
                second_longest = current
            current = i,
if len(current) > len(longest):
    second_longest = longest
    longest = current
elif len(current) > len(second_longest) and len(current) != len(longest):
    second_longest = current
                     
print(second_longest,len(second_longest))
