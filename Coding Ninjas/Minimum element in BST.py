'''
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''

def minVal(root):
    # Write your code here.
    if not root:
        return -1
    
    curr = root
    while curr.left:
        curr = curr.left
    
    return curr.data
