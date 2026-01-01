def kthElement(arr1, n, arr2, m, k):
    if n > m:
        return kthElement(arr2, m, arr1, n, k)

    low = max(0, k - m)
    high = min(k, n)

    while low <= high:
        x = (low + high) // 2
        y = k - x

        l1 = arr1[x-1] if x > 0 else float('-inf')
        l2 = arr2[y-1] if y > 0 else float('-inf')
        r1 = arr1[x] if x < n else float('inf')
        r2 = arr2[y] if y < m else float('inf')

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = x - 1
        else:
            low = x + 1
