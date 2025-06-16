def maximumFrequency(arr, n):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    max_freq = max(freq.values())
    return next(num for num in arr if freq[num] == max_freq)
