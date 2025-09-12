class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_len = 0
        max_frq = 0
        count = {}
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            max_frq = max(max_frq, count[s[r]])
            if r-l+1 - max_frq > k:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len
