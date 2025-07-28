def count(arr: [int], n: int, target: int) -> int:
    def lower_bound():
        left, right = 0, n - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                ans = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def upper_bound():
        left, right = 0, n - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                ans = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans

    first = lower_bound()
    last = upper_bound()
    return (last - first + 1) if first != -1 else 0
