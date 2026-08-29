# print("Traversal Of The Array")
arr = [4,7,2,9,3,6,8,1,5,7]
arr1 = [1,2,3,4,5,6,7,8,9,0]
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

def IfDuplicate(arr):
    Duplicate = False
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                Duplicate = True
    if Duplicate:
        print("Duplicates Present")
    else:
        print("Duplicates Not Present")

def DupliFreq(arr):
    element = ()
    freq = ()
    for i in range(len(arr)):
        count = 1
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if arr[i] not in element:
            freq += count,
            element += arr[i],
            print(element,"->",freq)

                
DupliFreq(arr)
            