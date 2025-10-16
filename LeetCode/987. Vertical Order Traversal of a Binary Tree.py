# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_map = defaultdict(list) 
        queue = deque([(root, 0, 0)])  

        while queue:
            node, row, col = queue.popleft()
            if node:
                col_map[col].append((row, node.val))
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))
        
        result = []
        for col in sorted(col_map.keys()):
            col_values = sorted(col_map[col], key=lambda x: (x[0], x[1]))
            result.append([val for row, val in col_values])
        return result
