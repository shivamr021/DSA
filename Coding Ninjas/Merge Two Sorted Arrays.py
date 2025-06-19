def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    n = len(a)
    m = len(b)
    union = []
    i, j = 0, 0
    while i < n and j < m:
        if a[i] <= b[j]:
            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != b[j]:
                union.append(b[j])
            j += 1

    while i < n:
        if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])
        i += 1

    while j < m:
        if len(union) == 0 or union[-1] != b[j]:
                union.append(b[j])
        j += 1

    return union
