class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        def largestRectangleArea(heights):
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

        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
