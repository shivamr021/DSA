class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def canShipedInDays(capacity):
            curr_load = 0
            D = 1

            for weight in weights:
                if curr_load + weight > capacity:
                    D += 1
                    curr_load = 0
                curr_load += weight
            
            return D <= days

        low, high = max(weights), sum(weights)

        while low < high: 
            capacity = (low + high) // 2

            if canShipedInDays(capacity):
                high = capacity
            else:
                low = capacity + 1
        return low
