from typing import *

def nextGreaterPermutation(A: List[int]) -> List[int]:
    n = len(A)
    idx = -1

    for i in range(n - 2, -1, -1):
        if A[i] < A[i + 1]:
            idx = i
            break

    if idx == -1:
        return A[::-1]

    for i in range(n - 1, idx, -1):
        if A[i] > A[idx]:
            A[i], A[idx] = A[idx], A[i]
            break

    A[idx + 1:] = reversed(A[idx + 1:])

    return A
