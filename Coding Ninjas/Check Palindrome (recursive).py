def isPalindrome(string: str) -> bool:
    def helper(s, l, r):
        if l >= r:
            return True

        if s[l] != s[r]:
            return False
            
        return helper(s, l + 1, r - 1)
    
    return helper(string, 0, len(string) - 1)
