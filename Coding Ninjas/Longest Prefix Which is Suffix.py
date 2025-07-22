def longestPrefixSuffix(s: str) -> str:
    # Write your code here.
    n = len(s)
    lps = [0] * n

    length = 0
    i = 1

    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    longest = lps[-1]
    return s[:longest] if longest != 0 else "-1"
