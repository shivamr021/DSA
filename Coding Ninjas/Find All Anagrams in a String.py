def findAnagramsIndices(st, pt, n, m):
    # Write your code here.
    res = []

    ptr_cnt = [0] * 26
    win_cnt = [0] * 26

    for ch in pt:
        ptr_cnt[ord(ch) - ord('A')] += 1

    for i in range(m):
        win_cnt[ord(st[i]) - ord('A')] += 1

    if win_cnt == ptr_cnt:
        res.append(0)

    for i in range(m, n):
        win_cnt[ord(st[i]) - ord('A')] += 1
        win_cnt[ord(st[i-m]) - ord('A')] -= 1 

        if win_cnt == ptr_cnt:
            res.append(i - m + 1)

    return res
