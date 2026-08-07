print("Remove Duplicates From List and give in set")
nums = [1,2,3,2,4,5,4,6,1,7,5]
n = set()
for i in nums:
    if i in nums:
        n.add(i)
print(n)