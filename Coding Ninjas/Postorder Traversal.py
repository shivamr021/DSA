'''
    Following is the structure of Tree Node

    class TreeNode:

        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
'''
from typing import List

def postorderTraversal(root) -> List[int]:
    # Write your code here.
    res = []

    def postOrder(node):
        if not node:
            return
        
        postOrder(node.left)
        postOrder(node.right)
        res.append(node.val)
    
    postOrder(root)
    return res
