class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def countSubarraysAtMost(k):
            if k < 0:
                return 0
            l = 0
            cnt = 0
            total = 0
            for r in range(len(nums)):
                total += nums[r]
                while total > k:
                    total -= nums[l]
                    l += 1
                cnt += r - l + 1
            return cnt
        return countSubarraysAtMost(goal) - countSubarraysAtMost(goal - 1)
