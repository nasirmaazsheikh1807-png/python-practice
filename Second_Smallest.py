print("Second Smallest Number Of The List")
n= [10,45,23,89,67,34]
smallest = n[1]
second_smallest= n[0]
for i in n:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    else:
        if i < second_smallest:
            second_smallest = i

print(second_smallest)
        