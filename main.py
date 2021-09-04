def linearSearch(item, myArray):
  for i in range(0, len(myArray)):
    if(myArray[i] == item):
      return i
  
  return -1

thearray = [1, 2, 6, 10, 13, 18, 20]


def binarySearch(item, myArray):
  low = 0
  high = len(myArray)-1
  ans = -1
  found = False
  while low <= high and found == False:
    mid = (low + high)//2
    if(myArray[mid] == item):
      found = True
      ans = mid
    elif(item < myArray[mid]):
      high = mid-1
    else:
      low = mid + 1
  return ans



def recursiveBinary(item, myArray, low, high):
  if(low > high):
    return -1
  else:
    mid = (low + high)//2
    if(myArray[mid] == item):
      return mid
    elif(item < myArray[mid]):
      high = mid - 1
    else:
      low = mid + 1
    
    return recursiveBinary(item, myArray, low, high)


print(recursiveBinary(10, thearray, 0, len(thearray)-1))



def bubbleSort(myArray):
  sorted = False
  while(sorted == False):
    sorted = True
    for x in range(0, len(myArray)-1):
      if(myArray[x] > myArray[x+1]):
        temp = myArray[x]
        myArray[x] = myArray[x+1]
        myArray[x + 1] = temp
        sorted = False
  return myArray


myNewArray = [8, 1, 4, 2, 9, 10, 3, 2]



def mergeSort(myArray):
  if(len(myArray) <= 1):
    return myArray
  else:
    mid = len(myArray)//2
    left = []
    right = []
    for x in range(0, mid):
      left.append(myArray[x])
    for y in range(mid, len(myArray)):
      right.append(myArray[y])
    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)
    combined = []
    leftPointer = 0
    rightPointer = 0
    while(leftPointer < len(sortedLeft) and rightPointer < len(sortedRight)):
      if(sortedLeft[leftPointer] < sortedRight[rightPointer]):
        combined.append(sortedLeft[leftPointer])
        leftPointer += 1
      else:
        combined.append(sortedRight[rightPointer])
        rightPointer += 1
    
    if(leftPointer < len(sortedLeft)):
      for x in range(leftPointer, len(sortedLeft)):
        combined.append(sortedLeft[x])
    elif(rightPointer < len(sortedRight)):
      for y in range(rightPointer, len(sortedRight)):
        combined.append(sortedRight[y])
    
    return combined


print(mergeSort(myNewArray))

