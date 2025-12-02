def divideTwoInteger(dividend: int, divisor: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = (dividend < 0) ^ (divisor < 0)

    dvd = abs(dividend)
    dvs = abs(divisor)

    quotient = 0

    for i in range(31, -1, -1):
        if (dvs << i) <= dvd:
            dvd -= (dvs << i)
            quotient += (1 << i)

    if negative:
        quotient = -quotient

    return max(INT_MIN, min(INT_MAX, quotient))
