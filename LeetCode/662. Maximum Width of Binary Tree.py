# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 0)])

        while queue:
            level_size = len(queue)
            _, first_index = queue[0]
            _, last_index = queue[-1]
            max_width = max(max_width, last_index - first_index + 1)

            for _ in range(level_size):
                node, idx = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * (idx - first_index)))
                if node.right:
                    queue.append((node.right, 2 * (idx - first_index) + 1))

        return max_width
