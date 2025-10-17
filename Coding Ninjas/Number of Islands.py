import sys 
sys.setrecursionlimit(10**7)

def numberOfIslands(grid, n, m):
    def dfs(r, c):
        if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0:
            return
        
        grid[r][c] = 0

        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),   # Up, Down, Left, Right
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals
        ]
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    cnt = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                dfs(r, c)
                cnt += 1
    return cnt


#   taking input using fast I/O
def takeInput() :
	n, m = map(int, sys.stdin.readline().strip().split(" "))
	grid = [list(map(int, sys.stdin.readline().strip().split(" "))) for row in range(n)]
	return n, m, grid

#   main
t = int(input().strip())
for i in range(t):
	n, m, grid = takeInput()
	ans = numberOfIslands(grid, n, m)
	print(ans)
