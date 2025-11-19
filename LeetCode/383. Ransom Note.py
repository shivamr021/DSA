from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cr = Counter(ransomNote)
        cm = Counter(magazine)

        return all(cm[c] >= cr[c] for c in cr)
