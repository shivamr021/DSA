def findIslands(mat, n, m):
    def dfs(r, c):
        if r < 0 or r >= n or c < 0 or c >= m or mat[r][c] == 0:
            return

        mat[r][c] = 0
		
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    dfs(r + dr, c + dc)

    count = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                dfs(i, j)
                count += 1
    return count
