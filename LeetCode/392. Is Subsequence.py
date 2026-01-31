class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        
        for char in t:
            if si < len(s) and s[si] == char:
                si += 1
        
        return si == len(s)
