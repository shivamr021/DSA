from math import prod

def findProductSumDifference(n: int) -> int:
    digits = [int(d) for d in str(n)]
    return prod(digits) - sum(digits)
