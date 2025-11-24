def maxDepth(s:str) -> int:
    # Write your code here.
    max_cnt = 0
    cnt = 0
    for ch in s:
        if ch == '(':
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        elif ch == ')':
            cnt -= 1
    
    return max_cnt
