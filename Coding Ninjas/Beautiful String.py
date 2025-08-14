def makeBeautiful(s):
    n = len(s)
    changes_start_0 = sum(s[i] != ('0' if i % 2 == 0 else '1') for i in range(n))
    changes_start_1 = sum(s[i] != ('1' if i % 2 == 0 else '0') for i in range(n))
    return min(changes_start_0, changes_start_1)
