from typing import List

def generateFibonacciNumbers(n: int) -> List[int]: 
    def fib_gen():
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    return list(fib_gen())
