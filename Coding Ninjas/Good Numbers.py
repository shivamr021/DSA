from typing import List

def goodNumbers(a: int, b:int, digit:int) -> List[int]:
    res = []

    for num in range(a, b + 1):
        s = str(num)

        if str(digit) in s:
            continue

        digits = [int(x) for x in s]
        good = True

        for i in range(len(digits) - 1):
            if digits[i] <= sum(digits[i + 1:]):
                good = False
                break

        if good:
            res.append(num)

    return res
