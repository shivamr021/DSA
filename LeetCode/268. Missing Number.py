class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0
        for i in range(n):
            res ^= nums[i]
        for i in range(1, n+1):
            res ^= i
        return res
        
