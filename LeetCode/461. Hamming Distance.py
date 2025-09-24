class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Brian Kernighan’s trick
        xor = x ^ y
        cnt = 0
        while xor:
            xor &= xor - 1   # clear lowest set bit
            cnt += 1
        return cnt
