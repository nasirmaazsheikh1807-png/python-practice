# print("Traversal Of The Array")
arr = [1,2,-3,-4,5,-6]
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

def PairSum(arr,target):
    pair = []
    for i in arr:
        for j in arr:
            if i + j == target:
                pair.append(i)
    print(pair)

def MajorityElement(arr):
    element = []
    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count += 1
    if count > len(arr)/2:
        print(i)

def Leader(arr):
    for i in range(len(arr)):
        leader = True
        for j in range(i+1, len(arr)):
            if arr[j]>arr[i]:
                leader = False
                break
        if leader:
            print(arr[i])
def LeaderW(arr): #Using While
    i = len(arr) - 1
    max = arr[i]
    print(arr[i])
    while i > 0:
        if arr[i] > max:
            max = arr[i]
            print(arr[i])
        i -= 1

def MaximumSubarr(arr):
    maxSum = 0
    for i in range(len(arr)):
        currentSum = 0
        for j in range(i, len(arr)):
            currentSum += arr[j]
            if currentSum > maxSum:
                maxSum = currentSum
    print("FINAL:",maxSum)

def MaxProfit(arr):
    maxProfit = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            currentProfit = arr[j] - arr[i]
            if currentProfit > maxProfit:
                maxProfit = currentProfit
    print("Maximum Profit:", maxProfit)

def MaxSubarr(arr):
    maxSum = 0
    currentSum = 0
    for i in arr:
        currentSum += i
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    print(maxSum)

def RotateArr(arr,num):
    new = [arr[-num],arr[num+2]]
    a = len(arr)-(num-1)
    for i in arr:
        arr.pop(-num)
        arr.pop(num+1)
        new.append(arr)
        break
    print(new)

def Rearrangearr(arr):
    new = []
    positive = []
    negative =[]
    for i in arr:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)
    i = 0
    p = 0
    n = 0
    while i < len(arr):
        if i % 2 == 0:
            new.append(positive[p])
            p += 1
        else:
            new.append(negative[n])
            n += 1
        i += 1
    print(new)        
Rearrangearr(arr)
        
    
        
        

