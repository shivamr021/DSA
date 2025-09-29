from collections import deque
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = {}

        # Phase 1: Build parent pointers
        def dfs(node, parent):
            if not node:
                return
            parent_map[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # Phase 2: BFS from target
        queue = deque([(target, 0)])
        visited = set([target])
        res = []

        while queue:
            node, dist = queue.popleft()

            if dist == k:
                res.append(node.val)
                continue

            for neighbor in (node.left, node.right, parent_map[node]):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

        return res
