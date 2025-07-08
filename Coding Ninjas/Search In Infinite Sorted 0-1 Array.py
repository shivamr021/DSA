def findFirstOne(get):
    low, high = 0, 1
    while get(high) == 0:
        low = high
        high *= 2 
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2
        if get(mid) == 1:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
