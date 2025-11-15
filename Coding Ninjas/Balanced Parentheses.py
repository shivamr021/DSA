from typing import *

def isBalanced(S: str) -> bool:
    d = {'(': ')', '{': '}', '[': ']'}
    st = []

    for ch in S:
        if ch in d:                   
            st.append(ch)
        else: 
            if not st:
                return False
            top = st.pop()
            if d[top] != ch:          
                return False

    return len(st) == 0
