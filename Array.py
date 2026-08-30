# print("Traversal Of The Array")
arr = [0,1,0,3,12]
arr1 = [1,2,3,4,5,6,7,8,9,0]
Max = arr[1]
secMax = arr[0]
secMin = arr[0]
Min = arr[1]
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
            print(element[i],"->",freq[i])

def ReverseArray(arr):
    i = len(arr)-1
    rev = []
    while i >= 0:
        rev.append(arr[i])
        i -= 1
    print(rev)

def SecondLargest(arr,Max,secMax):
    for i in arr:
        if i > Max:
            secMax = Max
            Max = i
        else:
            if i > secMax and Max != i:
                secMax = i
    print(secMax)

def SecondSmallest(arr,Min,secMin):
    for i in arr:
        if i < Min:
            secMin = Min
            Min = i
        else:
            if i < secMin and Min != i:
                secMin = i
    print(secMin)

def RemoveDuplicates(arr):
    new = []
    for i in arr:
        if i not in new:
            new.append(i)
    print(new)

def MissingNo(arr):
    Missing = []
    for i in range(1,6):
        for j in arr:
            if i not in arr:
                Missing.append(i)
                break
    print(Missing)

def MoveZeros(arr):
    count = 0
    for i in arr:
        if i == 0:
            count += 1
            arr.pop(arr[i])
    while count > 0:
        arr.append(0)
        count -= 1
    print(arr)

MoveZeros(arr)