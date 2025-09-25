def aggressiveCows(stalls, k):
    if k > len(stalls):
        return -1

    stalls.sort()

    def isMaxDist(min_dist):
        placed = 1
        last_pos = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i] - last_pos >= min_dist:
                placed += 1
                last_pos = stalls[i]
        return placed >= k

    low, high = 1, stalls[-1] - stalls[0]
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if isMaxDist(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result
