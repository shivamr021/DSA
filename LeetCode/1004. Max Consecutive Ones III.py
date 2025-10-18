class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        zeros = 0
        l, r = 0, 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                max_len = max(max_len, r-l+1)
            r += 1
        return max_len
