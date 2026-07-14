print("Even Odd Counter In List")
numbers= [10,45,23,89,67,34]
even = 0
odd = 0
for i in numbers:
    if i % 2==0:
        even += 1
    else:
        odd += 1
print(even)
print(odd)