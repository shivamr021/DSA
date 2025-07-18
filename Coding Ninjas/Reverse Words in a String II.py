def reverseOrderWords(s):
    # Write your code here.
    chars = list(s)

    def reverse(l, r):
        while l < r:
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1

    n = len(chars)
    reverse(0, n-1)

    start = 0
    for end in range(n+1):
        if end == n or chars[end] == ' ':
            reverse(start, end-1)
            start = end + 1
    
    return ''.join(chars)
