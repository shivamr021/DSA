from typing import List

def immediateSmaller(a: List[int]) -> None:
    # Write your code here
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i] = a[i+1]
        else:
            a[i] = -1
    a[-1] = -1
    return a
