class Solution(object):
    def myPow(self, x, n):
        res = 1.00000
        abs_n = abs(n)
        
        while abs_n > 0:
            if abs_n & 1:
                res *= x
            x *= x
            abs_n >>= 1
            
        return res if n >= 0 else 1 / res
