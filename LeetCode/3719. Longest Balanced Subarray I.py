class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            even_frq = {}
            odd_frq = {}

            for j in range(i, n):
                x = nums[j]

                if x % 2 == 0:
                    even_frq[x] = even_frq.get(x, 0) + 1
                else:
                    odd_frq[x] = odd_frq.get(x, 0) + 1

                if len(even_frq) == len(odd_frq):
                    max_len = max(max_len, j - i + 1)
            
        return max_len
