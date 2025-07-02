def totalStrings(s: str) -> int:
    # write your code here
    l, r = 0, 0
    cnt = 0
    chars = {}
    while r < len(s):
        chars[s[r]] = chars.get(s[r], 0) + 1
        while len(chars) > 2:
            chars[s[l]] -= 1
            if chars[s[l]] == 0:
                del chars[s[l]]
            l += 1
        cnt += (r-l+1)
        r += 1
    return cnt
