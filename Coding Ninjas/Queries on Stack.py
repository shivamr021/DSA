from os import *
from sys import *
from collections import *
from math import *

"""
	Here, queries[i] is a list of integer representing the ith query, 
	in which for different type of queries i.e -:
	1. PUSH 'X' -: queries[i][0] = 1, and queries[i][1] = 'X';
	2. POP -: queries[i][0] = 2;
	3. INC 'K', 'Y' -: queries[i][0] = 3, queries[i][1] = 'K' and queries[i][2] = 'Y';
"""

def answerQueries(queries, limit):
    # Write your code here.
	st = []
	res = []
  
	for query in queries:
		if query[0] == 1:
			x = int(query[1])
			if len(st) < limit:
				st.append(x)
		
		elif query[0] == 2:
			if st:
				res.append(st.pop())
			else:
				res.append(-1)
			
		elif query[0] == 3:
			k = query[1]
			y = query[2]
			for i in range(min(k, len(st))):
				st[i] += y

	return res
