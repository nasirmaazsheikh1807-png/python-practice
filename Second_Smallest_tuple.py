print("Second Smallest In Tuple")
n = (50,20,10,40,30)
second_smallest = n[0]
smallest = n[1]
for i in n:
    if i < smallest:
        i = smallest
        smallest = second_smallest

    else:
        if i < second_smallest:
            second_smallest = i
print(second_smallest)