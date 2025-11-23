class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        rem = len(s) % k
        if rem != 0:
            s += fill * (k - rem)
        ans = []
        for i in range(0, len(s), k):
            group = s[i:i+k]
            ans.append(group)
        return ans
