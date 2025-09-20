from os import *
from sys import *
from collections import *
from math import *

def theOrder(n):
	# Write your code here.
	q = deque(range(1,n+1))
	ans = []

	while q:
		q.append(q.popleft())

		ans.append(q.popleft())

	return ans	
