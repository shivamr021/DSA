class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7
        extra_days = n % 7
        
        total = 0
        for i in range(full_weeks):
            total += (7 * (1 + i)) + (7 * 6) // 2
        
        for i in range(extra_days):
            total += (1 + full_weeks) + i
        
        return total
