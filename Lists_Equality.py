print("Lists Are Equal Or Not")
a = list(map(int,input("Enter a List: ").split(",")))
b = list(map(int,input("Enter a List: ").split(",")))
count = 0
if len(a) != len(b):
    print("Lists Are Not Equal")
else:
    for i in range(3):
        if a[i] == b[i]:
            count += 1
        if count == len(a):
            print("Lists Are Equal")

        else:
            print("lists Are Not Equal")
            break
        