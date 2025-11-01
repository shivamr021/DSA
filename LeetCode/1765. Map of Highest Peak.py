from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        height = [[-1] * m for _ in range(n)]
        q = deque() 

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    q.append((i, j))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    q.append((nr, nc))
        
        return height
