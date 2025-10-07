'''
------- Binary Tree node structure -------
class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
'''

def largestBST(root):
    def helper(node):
        if not node:
            return True, 0, float('inf'), float('-inf')

        left_isBST, left_size, left_min, left_max = helper(node.left)
        right_isBST, right_size, right_min, right_max = helper(node.right)

        if left_isBST and right_isBST and left_max < node.data < right_min:
            size = left_size + right_size + 1
            return True, size, min(left_min, node.data), max(right_max, node.data)
        else:
            return False, max(left_size, right_size), 0, 0

    return helper(root)[1]
