def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    k %= len(arr)
    arr[:] = arr[k:] + arr[:k]
    return arr
