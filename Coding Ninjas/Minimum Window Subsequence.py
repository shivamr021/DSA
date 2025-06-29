def minWindow(S: str, T: str) -> str:
    n, m = len(S), len(T)
    min_len = float('inf')
    result = ""
    i = 0

    while i < n:
        
        tIdx = 0
        while i < n:
            if S[i] == T[tIdx]:
                tIdx += 1
                if tIdx == m:
                    break
            i += 1
        if tIdx < m:
            break  

        end = i  
        tIdx = m - 1
        while i >= 0:
            if S[i] == T[tIdx]:
                tIdx -= 1
                if tIdx < 0:
                    break
            i -= 1

        start = i
        window_len = end - start + 1
        if window_len < min_len:
            min_len = window_len
            result = S[start:end + 1]

        i = start + 1

    return result
