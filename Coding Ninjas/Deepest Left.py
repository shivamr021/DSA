from os import *
from sys import *
from collections import *
from math import *

'''
	Tree class Node structure.
	class TreeNode:
		def __init__(self, val):
			self.val = val
			self.left = None
			self.right = None
'''

def deepestLeftLeafNode(root):
	# Write you code here.
	best_lvl = best_val = 0

	def dfs(node, lvl, isLeft):
		nonlocal best_lvl, best_val

		if not node:
			return
		
		if isLeft and not node.left and not node.right:
			if lvl > best_lvl:
				best_lvl = lvl
				best_val = node.val
			elif lvl == best_lvl:
				best_val = max(best_val, node.val)
	
		dfs(node.left, lvl + 1, True)
		dfs(node.right, lvl + 1, False)
	
	dfs(root, 1, False)

	return best_val
