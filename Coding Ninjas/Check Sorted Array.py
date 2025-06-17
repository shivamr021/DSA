def isSorted(n: int,  a: [int]) -> int:
    # Write your code here.
    for i in range(1, n):
        if a[i-1] > a[i]:
            return 0
    return 1
