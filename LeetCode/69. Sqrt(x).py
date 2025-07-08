class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        i = 1
        sq = i * i
        while x >= sq:
            i += 1
            sq = i * i
        return int(i-1)
