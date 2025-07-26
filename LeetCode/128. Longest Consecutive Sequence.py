class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        longest = 1
        
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                cnt = 1
                x = num
                while x + 1 in nums_set:
                    cnt += 1
                    x += 1
                longest = max(longest, cnt)

        return longest
