from typing import List

def getLongestZeroSumSubarrayLength(arr: List[int]) -> int:
    seen = {0: -1}
    longest = 0
    preSum = 0

    for i in range(len(arr)):
        preSum += arr[i]
        if preSum in seen:
            longest = max(longest, i - seen[preSum])
        else:
            seen[preSum] = i
    return longest
