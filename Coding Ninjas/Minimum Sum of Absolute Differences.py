def minimumSum(arr1, arr2, n):
	# Write your code here.
	arr1.sort()
	arr2.sort()
  min_diff = sum(abs(a - b) for a, b in zip(arr1, arr2))
	return min_diff
