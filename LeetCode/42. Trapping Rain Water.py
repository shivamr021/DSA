class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lMax = rMax = total = 0
        l, r = 0, n-1
        
        while l < r:
            if height[l] <= height[r]:
                if lMax > height[l]:
                    total += lMax - height[l]
                else:
                    lMax = height[l]
                l += 1
            else:
                if height[r] < rMax:
                    total += rMax - height[r]
                else:
                    rMax = height[r]
                r -= 1
        return total
