class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n, m = len(nums1), len(nums2)
        total = n + m
        left_size = (total + 1) // 2
        
        low, high = 0, n

        while low <= high:
            x = (low + high) // 2
            y = left_size - x

            left1 = nums1[x - 1] if x > 0 else float('-inf')
            right1 = nums1[x] if x < n else float('inf')

            left2 = nums2[y - 1] if y > 0 else float('-inf')
            right2 = nums2[y] if y < m else float('inf')

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            
            elif left1 > right2:
                high = x - 1
            
            else:
                low = x + 1
