# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def getHeight(node, goLeft=True):
            height = 0
            while node:
                height += 1
                node = node.left if goLeft else node.right
            return height
            
        left_height = getHeight(root, True)
        right_height = getHeight(root, False)
        if left_height == right_height:
            return (1 << left_height) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
