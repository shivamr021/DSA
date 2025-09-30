from os import *
from sys import *
from collections import *
from math import *

'''
Following is the Binary Tree node class

class TreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        
        if (self.left):
            del self.left

        if (self.right):
            del self.right
'''

def countNodes(root):
    # write your code here
    if not root:
        return 0
    
    def get_height(node, go_left = True):
        height = 0
        while node:
            height += 1
            node = node.left if go_left else node.right
        return height
    
    left_height = get_height(root, True)
    right_height = get_height(root, False)

    if left_height == right_height:
        return (1 << left_height) - 1
    else:
        return 1 + countNodes(root.left) + countNodes(root.right)
