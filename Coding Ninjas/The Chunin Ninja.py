# from os import *
# from sys import *
# from collections import *
# from math import *
from typing import *

def chuninNinja(n: int, m: int, arr: List[int]) -> List[int]:
	# Write your code here.
	row_mins = [min(row) for row in arr]

	col_max = [max(arr[i][j] for i in range(n)) for j in range(m)]

	ans = []
	for i in range(n):
		for j in range(m):
			if arr[i][j] == row_mins[i] and arr[i][j] == col_max[j]:
				ans.append(arr[i][j])
	
	return ans
