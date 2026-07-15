print("Smallest Number Of The List")
n= [10,45,23,89,67,34]
smallest = n[1]
for i in n:
    if i < smallest:
        smallest = i

print(smallest)
        