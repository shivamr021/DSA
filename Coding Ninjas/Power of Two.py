def isPowerOfTwo(n:int) -> bool:
    # Write your code here
    return n > 0 and (n & (n - 1)) == 0
