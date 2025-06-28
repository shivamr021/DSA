def searchInsert(arr: [int], m: int) -> int:
    # Write your code here.
    n = len(arr)
    start, end = 0, n-1
    ans = n
    while start <= end:
        mid = start + (end-start) // 2

        if arr[mid] >= m:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans
