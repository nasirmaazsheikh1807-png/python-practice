print("Largest Number in Tuple")
n = (15,7,90,32,11)
largest = (0)
smallest = (15)
for i in n:
    if i > largest:
        largest = i
    if i < smallest:
            smallest = i 

print(largest , smallest)