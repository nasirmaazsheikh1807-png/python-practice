print("Frequency of the number in the tuple")
n = (5,2,5,8,5,1)
count = (0)
for i in n:
    if i == 5:
        count += 1
print(f"5 occurs {count} times in the given Tuple")