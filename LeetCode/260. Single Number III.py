class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        
        rightmost = (xor & xor-1) ^ xor
        b1 = b2 = 0

        for num in nums:
            if rightmost & num:
                b1 ^= num
            else:
                b2 ^= num
        return [b1,b2]
