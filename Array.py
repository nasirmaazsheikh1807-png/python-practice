# print("Traversal Of The Array")
arr = [8,3,15,2,11,6]
Max = arr[0]
Min = arr[0]
# for i in range(len(arr)):
#     print(i,arr[i])

# Linear Search in Normal :
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("Found The Target Index: ",i)
#         break
# else:
#     print("Target NOt Found!")

# Linear Search As A Function:
def LinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Found The Target Index:{i}"
    else:
        return -1

def MaxElement(arr, Max):
    for i in arr:
        if i > Max:
            Max = i
    print("MaxElement Is :",Max)

def MaxElementIdx(arr, Max):
    for i in range(len(arr)):
        if arr[i] > Max:
            Max = i
    print("Found The MaxElement Index:",Max)
            
def MinElementIdx(arr, Mini):
    for i in range(len(arr)):
        if arr[i] < Mini:
            Min = i
            Mini = arr[i]
    print("Found The MinElement:",Min)

MinElementIdx(arr, Min)