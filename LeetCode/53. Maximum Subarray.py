class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = float('-inf')
        curSum = 0

        for i in range(len(nums)):
            curSum += nums[i]
            
            if curSum > maxSum:
                maxSum = curSum

            if curSum < 0:
                curSum = 0
        return maxSum
            
