class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for row in range(1, numRows + 1):
            ans = 1
            ansRow = [1]
            for col in range(1, row):
                ans *= (row - col)
                ans //= col
                ansRow.append(ans)
            res.append(ansRow)
        
        return res
