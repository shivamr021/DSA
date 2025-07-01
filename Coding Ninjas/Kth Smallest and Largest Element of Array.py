import heapq

def kthSmallLarge(arr, n, k):
    def kth_largest(arr, k):
        min_heap = []
        for num in arr:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
    
    def kth_smallest(arr, k):
        max_heap = []
        for num in arr:
            heapq.heappush(max_heap, -num)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return -max_heap[0]

    return (kth_smallest(arr, k), kth_largest(arr, k))
