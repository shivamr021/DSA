def count_subarrays_with_max_in_range(arr, X, Y):
    def count_at_most(K):
        count = 0
        l = 0
        for r in range(len(arr)):
            if arr[r] > K:
                l = r + 1
            count += (r - l + 1)
        return count

    return count_at_most(Y) - count_at_most(X - 1)
