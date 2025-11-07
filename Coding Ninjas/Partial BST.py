from os import *
from sys import *
from collections import *
from math import *
import queue
import sys
sys.setrecursionlimit(10**6)

class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
        

def validateBST(root):
    def helper(node, min_val, max_val):
        if node is None:
            return True
        
        if node.data < min_val or node.data > max_val:
            return False
        
        left_valid = helper(node.left, min_val, node.data)
        right_valid = helper(node.right, node.data, max_val)
        
        return left_valid and right_valid
    
    return helper(root, float('-inf'), float('inf'))


def buildLevelTree(levelorder):
    
    index = 0
    length = len(levelorder)
    
    if length<=0 or levelorder[0]==-1:
        return None
    
    
    root = BinaryTreeNode(levelorder[index])
    index += 1
    
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        
        if leftChild != -1:
            
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
            
        rightChild = levelorder[index]
        index += 1
        
        
        if rightChild != -1:
            
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
            
            
    return root
    

t = int(sys.stdin.readline().strip())
while t >0:
    
    
    li = list(map(int, sys.stdin.readline().strip().split(" ")))
    root = buildLevelTree(li)
    if (validateBST(root)):
        print('true')
    else:
        print('false')
    t = t -1
