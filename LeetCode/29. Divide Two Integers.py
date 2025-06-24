class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == divisor:
            return 1
            
        if divisor == 0:
            return float('inf') 

        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        sign = (dividend >= 0) == (divisor >= 0)
        n = abs(dividend)
        d = abs(divisor)
        quotient = 0

        while d <= n:
            cnt = 0
            while n >= (d << (cnt + 1)):
                cnt += 1
            quotient += 1 << cnt
            n -= d << cnt

        result = quotient if sign else -quotient
        return min(max(-2**31, result), 2**31 - 1)
