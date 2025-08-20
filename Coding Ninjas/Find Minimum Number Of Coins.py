from typing import List

def MinimumCoins(n: int) -> List[int]:
    # write your code here
    coins = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    ans = []

    for coin in coins:
        while n >= coin:
            ans.append(coin)
            n -= coin
    return ans
