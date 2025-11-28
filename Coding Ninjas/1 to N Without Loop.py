from typing import List

def printNos(x: int) -> List[int]: 
    
    def solve(n):
        if n == 0:
            return []
        arr = solve(n - 1)
        arr.append(n)
        return arr
    
    return solve(x)
