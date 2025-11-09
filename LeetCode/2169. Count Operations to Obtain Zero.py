class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        cnt = 0
        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            cnt += 1
        return cnt
