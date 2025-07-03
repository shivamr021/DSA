def NthRoot(n: int, m: int) -> int:
    low, high = 0, m

    while low <= high:
        mid = (low + high) // 2
        power = mid ** n

        if power == m:
            return mid
        elif power < m:
            low = mid + 1
        else:
            high = mid - 1

    return -1
