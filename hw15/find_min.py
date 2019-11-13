def findMinUtil(arr, low, high, n):

    # Find index of middle element
    # (low + high)/2
    mid = low + (high - low)/2
    mid = int(mid)

    # Compare middle element with its
    # neighbours (if neighbours exist)
    if ((mid == 0 or arr[mid - 1] >= arr[mid]) and (mid == n - 1 or arr[mid + 1] >= arr[mid])):
        return mid 
 
    elif (mid > 0 and arr[mid - 1] < arr[mid]): 
        return findMinUtil(arr, low, (mid - 1), n) 
  
    else: 
        return findMinUtil(arr, (mid + 1), high, n)

def findMin(arr, n): 
    
    index = findMinUtil(arr, 0, n - 1, n)

    return arr[index]

print(findMin([56, 43, 32, 21, 23, 25, 57], 7))
