# print("Traversal Of The Array")
arr =[1,2,3,0,0,0]
arr1 = [2,5,6]
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

def LongConSubArr(arr,k):
    MaxArr = 0
    for i in range(len(arr)):
        sum = 0
        currentArr = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            if sum <= k:
                currentArr += 1
                if currentArr > MaxArr:
                    MaxArr = currentArr
            elif sum > k:
                currentArr = 0
                sum = 0
        
    print(MaxArr)

def Equalzerones(arr):
    zero = 0
    one = 0
    idx = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zero += 1
        elif arr[i] == 1:
            one += 1
        
            if zero == one:
                idx = i
    print(idx)

def LongSubArrDiv(arr,k):
    MaxArr = 0
    for i in range(len(arr)):
        currentArr = 0
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            currentArr += 1
            if sum % k == 0:
                if currentArr > MaxArr:
                    MaxArr = currentArr
    print(MaxArr)

def MaxSumCons(arr,k):
    MaxSum = 0
    for i in range(len(arr)):
        CurrentSum = 0
        j = 0
        while j <= k:
            CurrentSum += arr[j]
            j += 1
            if CurrentSum > MaxSum:
                MaxSum = CurrentSum
    print(MaxSum)

def MaxSumConsn(arr,k):
    MaxSum = 0
    CurrentSum = 0
    prevSum = 0
    for i in range(k):
        prevSum += arr[i]
        if CurrentSum > MaxSum:
            MaxSum = CurrentSum
    for j in range(k,len(arr)):
        CurrentSum = prevSum - arr[j-k] + arr[j]
        prevSum = CurrentSum
        if CurrentSum > MaxSum:
            MaxSum = CurrentSum
    
    print(MaxSum)

def MaxAvgSub(arr,k):
    CurrentAvg = 0
    MaxAvg = 0
    prevSum = 0
    currentSum = 0
    for i in range(k):
        prevSum += arr[i]
        prevAvg = prevSum/k
    for j in range(k,len(arr)):
        currentSum = prevSum - arr[j-k] + arr[j]
        CurrentAvg = currentSum/k
        prevSum = currentSum
        if CurrentAvg > MaxAvg:
            MaxAvg = CurrentAvg
    print(MaxAvg)

def LongestSubArr(arr,k):
    sum = 0
    sub = []
    MaxSub = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum <= k:
            sub.append(arr[i])
            if len(sub) > MaxSub:
                MaxSub = len(sub)
        while sum >= k:
            sub.pop(0)
            sum -= i
    print(MaxSub)

def LongSubArrKzero(arr,k):
    sub = []
    MaxSub = 0
    one = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zero += 1
        if arr[i] == 1:
            one += 1
        if zero <= k:
            sub.append(arr[i])
            if len(sub) > MaxSub:
                MaxSub = len(sub)
            while zero >= k:
                sub.remove(0)
                zero -= 1
    print(MaxSub)

def LongSubDistinct(arr,k):
    sub = []
    MaxSub = 0
    for i in range(len(arr)):
        sub.append(arr[i])
        while len(set(sub)) > k:
            sub.pop(0)   
            if len(sub) > MaxSub:
                MaxSub = len(sub)
    print(MaxSub)

def FreqCounterDict(arr):
    freq = {}
    for i in arr:
        if 0 <= i <= 9:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
    print(freq)
def NonRepEle(arr):
    new = {}
    for i in arr:
        if 0 <= 1 <= 9:
            if i in new:
                new[i] += 1
            else:
                new[i] = 1
    for key,value in new.items():
        if value == 1:
            print(key)
            break
def TwoSum(arr,target):
    new = {}
    for i in arr:
        if target - i in new:
            print(target-i , i)
        else:
            new[i] = i

def CountPairSum(arr,target):
    new = {}
    count = 0
    for i in arr:
        if target - i in new:
            new[i] = target - i
            count += 1
        else:
            new[i] = i
    print(count)

def MajorityElement(arr):
    freq = {}
    n = len(arr)
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
        if freq[i] > n/2:
            print(i)

def FirstRepElement(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
        if freq[i] == 2:
            print(i)
            break

def FindMissNo(arr):
    MissingNo = 0
    freq = {}
    for i in range(len(arr) + 1):
        if i in freq:
            freq[i] += i
        else:
            freq[i] = i
        if freq[i] not in arr:
            MissingNo += i
    print(MissingNo)

def LongConsSeq(arr):
    freq = {}
    count = 0
    for i in arr:
        if i in freq:
            freq[i] += i
        else:
            freq[i] = 1
    for key,value in freq.items():
        if key and  key + 1 in arr:
            count += 1
    print(count + 1)

def Twosum(arr,target):
    new = {}
    partner = 0
    for i in arr:
        if  target - i in new:
            partner = target- i
            print(i, partner)
        else:
            new[i] = i

def SubSum(arr,k):
    prefix = 0
    new = {0:1}
    for  i,value in enumerate(arr):
        prefix += value
        previous = prefix - k 
        if prefix - k  in new:
            start = new[prefix-k]+1
            print(arr[start:i+1])

        if prefix not in new:
            new[prefix] = i

def SubSumCount(arr,target):
    new = {0:-1}
    prefix = 0
    count = 0
    for i,value in enumerate(arr):
        prefix += value
        previous = prefix - target
        if prefix - target in new:
            start = new[prefix-target]+1
            print(len(arr[start:i+1]))
            count += 1
        if prefix not in new:
            new[prefix] = i
    print("#",count)

def SubSumDiv(arr,target):
    new = {0:1}
    prefix = 0
    count = 0
    for i,value in enumerate(arr):
        prefix += value
        reminder = prefix % target
        if reminder in new:
            start = new[prefix % target]+1
            print((arr[start:i+1]))
            count += 1
        if reminder not in new:
            new[reminder] = count
    print("#",count)

def Twosumm(arr,target):
    result = []
    new = {}
    for i,value in enumerate(arr):
        element = target - value
        if target - value in new:
            result.append(i)
            result.append(new[element])
        else:
            new[value] = i
    print(result)

def TwoPointerTwoSum(arr,Target):
    left = 0
    right = len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == Target:
            print(left , right)
            break
        elif total > Target:
            right -= 1
        elif total < Target:
            left += 1
        else:
            print("Error Target Not found!")

def TwoPointerRemDuplicate(arr):
    place = 0
    res = 1
    check = 1
    while check < len(arr):
        if arr[check] != arr[place]:
            place += 1
            arr[place] = arr[check]
            res += 1
        check += 1
        
    return arr[:res]
result = TwoPointerRemDuplicate(arr)
print(result)

def SquareSortedArr(arr):
    neg = []
    pos = []
    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    #Case 1 : If no neg element:
    if len(neg) == 0:
        return [x*x for x in pos]
    #Case 2: If no pos Element:
    if len(pos) == 0:
        neg = [x*x for x in neg]
        neg.reverse()
        return neg
    #Case 3: If Both Pos And Neg Element present:
    neg = [x*x for x in neg][::-1]
    pos = [x*x for x in pos]
    res = []
    n,m = len(neg) , len(pos)
    i = j = 0
    while i < n and j < m:
        if neg[i] <= pos[j]:
            res.append(neg[i])
            i += 1
        else:
            res.append(pos[j])
            j += 1
    while i < n:
        res.append(neg[i])
        i += 1
    while j < m:
        res.append(pos[j])
        j += 1
    return res

def MergeSortedArr(arr,arr1):
    k = 5
    i = j = 2
    while i >= 0 and j >= 0:
        if arr[i] >= arr1[j]:
            arr[k] = arr[i]
            i -= 1
        else:
            arr[k] = arr1[j]
            j -= 1
        k -= 1
    while j >= 0:
        arr[k] = arr[j]
        j -= 1
        k -= 1
    while i > = 0:
        arr[k] = arr[i]
        i -= 1
        k -= 1
    return arr
result = MergeSortedArr(arr,arr1)
print(result)



            

        

