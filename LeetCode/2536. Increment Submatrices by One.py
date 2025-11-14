class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """

        # Step 1: Create a difference matrix
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # Step 2: Apply each query using 2D difference trick
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            if c2 + 1 < n:
                diff[r1][c2 + 1] -= 1
            if r2 + 1 < n:
                diff[r2 + 1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                diff[r2 + 1][c2 + 1] += 1

        # Step 3: Convert difference matrix → actual values via prefix sums
        # Row-wise prefix sum
        for r in range(n):
            for c in range(1, n):
                diff[r][c] += diff[r][c - 1]

        # Column-wise prefix sum
        for c in range(n):
            for r in range(1, n):
                diff[r][c] += diff[r - 1][c]

        # Step 4: Extract actual n x n matrix
        result = [row[:n] for row in diff[:n]]
        return result
