class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        new_heights = heights + [0]

        for i, h in enumerate(new_heights):
            while stack and new_heights[stack[-1]] > h:
                top = stack.pop()
                height = new_heights[top]
                nse = i
                pse = stack[-1] if stack else -1
                width = nse - pse - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
