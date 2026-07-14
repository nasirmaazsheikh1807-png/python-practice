print("Second Largest Number in the List")
numbers= [10,45,23,89,67,34]
largest = numbers[1]
second_largest = numbers[0]
for i in numbers:
    if i>largest:
        second_largest = largest
        largest = i
    else:
        if i > second_largest:
            second_largest=i
print(second_largest)
