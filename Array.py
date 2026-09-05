# print("Traversal Of The Array")
arr = [100,4,200,1,3,2]
arr1 = [1,1,0,1,1,1,0,1]
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

def RemoveDuplicates(arr):
    new = []
    for i in arr:
        if i not in new:
            new.append(i)
    print(new)

def SecLargest(arr):
    largest = arr[0]
    sec_largest = arr[1]
    for i in arr:
        if i > largest:
            sec_largest = largest
            largest = i
        else:
            if i > sec_largest and largest != i:
                sec_largest = i
    print(sec_largest)

def FindMissingNo(arr):
    missing = []
    for i in range(1,len(arr)):
        if i not in arr:
            missing.append(i)
            break
    print(missing)

def DupliElement(arr):
    element = []
    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        if count > 1 and i not in element:
            element.append(i)
    print(element)
def ArrIntersection(arr1,arr2):
    Intersection = []
    for i in arr1:
        for j in arr2:
            if i == j:
                Intersection.append(i)
    print(Intersection)

def FirstDuplicate(arr):
    element = []
    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        if count > 1 and i not in element:
            element.append(i)
            break
    print(element)

def MaxConsecutive(arr):
    Max = 0
    prev = arr[0]
    count = 0
    for i in arr:

        if prev == i:
            count += 1
            prev = i
            if count > Max:
                Max = count
        else:
            count = 0   
    print(Max)
def EquilibriumIdx(arr):
    idx = []
    for i in range(len(arr)):
        left = 0
        for j in range(i):
            left += arr[j]

        right = 0
        for j in range(i+1,len(arr)):
            right += arr[j]
        if left == right:
            idx.append(i)
    print(idx)  


def ProductArr(arr):
    result = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i == j:
                continue
            else:
                product *= arr[j]
        result.append(product)
    print(result)

def RotateArrRight(arr, k):
    for i in range(k):
        x = arr.pop()
        arr.insert(0,x)
    print(arr)

def RotateArrLeft(arr, k):
    for i in range(k):
        x = arr.pop(0)
        arr.append(x)
    print(arr)


def MaxConsOnesFlip(arr):
    flip = True
    k = 1
    Max = 0
    prev = arr[0]
    count = 0
    for i in arr:
        if prev == i:
            count += 1
            prev = i
            if count > Max:
                Max = count
        elif i == 0 and flip:
            i = 1
            count += 1
            flip = False
        else:
            count = 0
    print(Max)

def SubArrSum(arr, Target):
    sub = []
    for i in range(len(arr)):
        currentArr = 0
        for j in range(i,len(arr)):
            currentArr += arr[j]
            if currentArr > Target:
                currentArr = 0
            else:
                if currentArr == Target:
                    for k in range(i,j+1):
                        sub.append(arr[k])
    print(sub)

def SubArrProd(arr, Target):
    sub = []
    for i in range(len(arr)):
        currentArr = 1
        for j in range(i, len(arr)):
            currentArr *= arr[j]
            if currentArr > Target:
                currentArr = 0
            else:
                if currentArr == Target:
                    for k in range(i,j+1):
                        sub.append(arr[k])
    print(sub)
def LongConsSeq(arr):
    seq = []
    count = 0
    for i in range(len(arr)):
        for j in arr:
            if i == j:
                count += 1
                if count > 1 and j+1 in arr:
                    seq.append(j)
                else:
                    seq.append(j)
    print(len(seq))
LongConsSeq(arr)                

