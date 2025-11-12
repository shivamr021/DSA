def calcGDC(n:int, m: int) -> int:
    while m > 0:
        n, m = m, n%m
    return n
