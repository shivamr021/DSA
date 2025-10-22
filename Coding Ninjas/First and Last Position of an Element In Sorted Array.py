def firstAndLastPosition(arr, n, k):
    def firstOcc(arr, n, k):
        low, high = 0, n - 1
        first = -1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == k:
                first = mid
                high = mid - 1
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return first
    

    def lastOcc(arr, n, k):
        low, high = 0, n - 1
        last = -1
        while low <= high:
            mid = low + (high - low) // 2 
            if arr[mid] == k:
                last = mid
                low = mid + 1 
            elif arr[mid] > k: 
                high = mid - 1
            else:
                low = mid + 1
        return last

    first = firstOcc(arr,n,k)
    if first == -1:
        return -1, -1
    last = lastOcc(arr,n,k)
    
    return first, last
