from itertools import takewhile
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = -1 if s[0] == '-' else 1
        if s[0] in ['-', '+']:
            s = s[1:]

        digits = ''.join(takewhile(str.isdigit, s))

        if not digits:
            return 0

        num = sign * int(digits)
        return max(min(num, 2**31 - 1), -2**31)
