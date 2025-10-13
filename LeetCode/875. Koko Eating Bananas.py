class Solution(object):
    def minEatingSpeed(self, piles, h):
        
        def can_eat_all(s):
            return sum((pile + s - 1) // s for pile in piles) <= h

        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            if can_eat_all(mid):
                result = mid 
                right = mid - 1
            else:
                left = mid + 1 

        return result
