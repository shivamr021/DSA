def getFourthLargest(arr, n):
    # Sort in descending order
    arr.sort(reverse=True)
    
    # Check if 4th element exists
    if n >= 4:
        return arr[3]
    else:
        return -2147483648
