def maximumFrequency(arr, n):
	# Write your code here.
	frq = {}
	first_occ = {}

	max_frq = 0
	ans = arr[0]

	for i, num in enumerate(arr):
		frq[num] = frq.get(num, 0) + 1

		if num not in first_occ:
			first_occ[num] = i

		if frq[num] > max_frq:
			max_frq = frq[num]
			ans = num

		elif frq[num] == max_frq:
			if first_occ[num] < first_occ[ans]:
				ans = num
	
	return ans
