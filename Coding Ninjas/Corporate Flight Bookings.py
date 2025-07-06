from os import *
from sys import *
from collections import *
from math import *

def corpFlightBookings(bookings, n):
	# Write your code here.
	ans = [0] * n
	for first, last, seats in bookings:
		ans[first-1] += seats
		if last < n:
			ans[last] -= seats
		
	for i in range(1, n):
		ans[i] += ans[i-1]
	
	return ans
