class Solution:
    def minPartitions(self, n: str) -> int:
        max = float('-inf')
        for i in n:
            if int(i) > max:
                max = int(i)
        return max
