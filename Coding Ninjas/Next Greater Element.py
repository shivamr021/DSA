from typing import List

def nextGreaterElement(arr, n):
    nge = [-1] * n
    stack = []

    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            nge[i] = stack[-1]

        stack.append(arr[i])

    return nge
