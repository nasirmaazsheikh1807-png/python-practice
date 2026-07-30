print("Find The Longest Consecutive Streak")
n = (1,1,1,2,2,5,5,5,5,3,3,3)
streak = ()
element = n[0],
count = 0
previous = n[0]
for i in n:
    if element[-1] == i:
        count += 1
    if element[-1] != i:
        element += i,
        streak += count,
        count = 1
streak += count,
highest = streak[0]
num = element[0]
for i,j in enumerate(streak):
    if j > highest:
        highest = j
        num = element[i]

print(f"Number: {num} , Streak : {highest}")