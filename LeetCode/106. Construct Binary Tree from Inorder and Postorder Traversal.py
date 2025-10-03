# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : idx for idx, val in enumerate(inorder)}

        self.post_idx = len(postorder) - 1

        def arrayToTree(left, right):
            if left > right:
                return None
            
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            mid = inorder_map[root_val]
            root.right = arrayToTree(mid + 1, right)
            root.left = arrayToTree(left, mid - 1)

            return root

        return arrayToTree(0, len(inorder) - 1)
