class Solution:
    def isValid(self, s: str) -> bool:
        mydict = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in mydict.values(): 
                stack.append(char)
            else: 
                if not stack or stack.pop() != mydict[char]:
                    return False
        return not stack 
