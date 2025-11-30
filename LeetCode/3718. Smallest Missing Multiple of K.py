class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiples = set(nums)
        i = 1
        while True:
            mult = i * k
            if mult not in multiples:
                return mult
            i += 1
