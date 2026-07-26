print("Second Largest Number in The Tuple")
n = (12,45,7,45,32,19)
second_largest = n[0]
largest = n[1]
for i in n:
    if i > largest:
        second_largest = largest
        largest = i
    else:
        if i > second_largest and i != largest:
            second_largest = i 
print(second_largest)