def pairSum(arr, s):
    arr.sort()  # sort array for consistent ordering
    result = []

    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == s:
                result.append([arr[i], arr[j]])

    return result
