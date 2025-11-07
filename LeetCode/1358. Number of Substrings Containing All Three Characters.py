class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = [-1] * 3
        cnt = 0
        for i in range(len(s)):
            last_seen[ord(s[i]) - ord('a')] = i
            cnt += 1 + min(last_seen)
        return cnt
