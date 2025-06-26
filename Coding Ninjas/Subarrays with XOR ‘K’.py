def subarraysWithSumK(a: [int], b: int) -> int:
    seen = {0: 1}
    preXOR = 0
    cnt = 0

    for num in a:
        preXOR ^= num
        cnt += seen.get(preXOR ^ b, 0)
        seen[preXOR] = seen.get(preXOR, 0) + 1
        
    return cnt
