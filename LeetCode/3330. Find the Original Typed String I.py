class Solution:
    def possibleStringCount(self, word: str) -> int:
        groups = [(char, sum(1 for _ in group)) for char, group in groupby(word)]
    
        total = 1  
        for char, count in groups:
            if count > 1:
                total += count - 1  
        return total
