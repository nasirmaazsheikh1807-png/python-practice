print("Counting Frequency in a String")
n = str(input("Enter a String: "))
freq = ("")
for i in n:
    count = 0
    for j in n:
        if i == j:
            count += 1
    if i not in freq:
        print(i , "->" , count)
        freq += i

    
