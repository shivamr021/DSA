def removeDuplicates(arr,n):
    # Write your code here.
    i = 0
    for j in range(n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return len(arr[:i+1])
