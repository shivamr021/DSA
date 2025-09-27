class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        if num < 0:
            num += 1 << 32 
        
        hex_chars = "0123456789abcdef"
        result = ""
        
        while num > 0:
            digit = num % 16
            result = hex_chars[digit] + result
            num //= 16
        
        return result
