from os import *
from sys import *
from collections import *
from math import *

def findSmallestWithKSwaps(arr, n, k):

	# Write your code here
	for i in range(n):
		pos = i
		for j in range(i+1,min(n,i+k+1)):
			if arr[j] < arr[pos]:
				pos = j

		for j in range(pos,i,-1):
			arr[j],arr[j-1] = arr[j-1],arr[j]

		k -= (pos-i)

		if k<=0:
			break

	return arr					
