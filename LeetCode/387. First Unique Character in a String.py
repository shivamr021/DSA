from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frq = Counter(s)

        for i in range(len(s)):
            if frq[s[i]] == 1:
                return i
        
        return -1
