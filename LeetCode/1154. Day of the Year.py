class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        
        if is_leap:
            days[1] = 29
        
        return sum(days[:month-1]) + day
