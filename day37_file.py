count = 1
with open("day37.txt","r") as file:
    for line in file:
        print(count, "-", line)
        count += 1