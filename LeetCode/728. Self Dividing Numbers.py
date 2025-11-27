class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(n):
            x = n
            while x > 0:
                d = x % 10
                if d == 0 or n % d != 0:
                    return False
                x //= 10
            return True

        ans = []
        for num in range(left, right + 1):
            if isSelfDividing(num):
                ans.append(num)
        return ans
