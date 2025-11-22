class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        for ch in s:
            if 'A' <= ch <= 'Z': 
                res.append(chr(ord(ch) + (ord('a') - ord('A'))))
            else:
                res.append(ch)
        return "".join(res)
