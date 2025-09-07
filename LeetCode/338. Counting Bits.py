class Solution(object):
    def noOfSetBits(self, n):
        cnt = 0
        while n:
            n = n & n-1
            cnt += 1
        return cnt
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n+1):
            ans.append(self.noOfSetBits(i))
        return ans
