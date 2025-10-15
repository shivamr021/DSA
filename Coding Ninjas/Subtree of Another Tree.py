'''
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def isSubtree(T, S):
    def isIdentical(root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return (root1.data == root2.data and 
                isIdentical(root1.left, root2.left) and 
                isIdentical(root1.right, root2.right))
    
    if not S:
        return True
    if not T:
        return False
    if isIdentical(T, S):
        return True
    return isSubtree(T.left, S) or isSubtree(T.right, S)
