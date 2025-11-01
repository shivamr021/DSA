from collections import deque

def wallsAndGates(a, n, m): 
    # Write your Code here.
    q = deque()
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                q.append((i, j))
    
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]

    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and a[nr][nc] == 2147483647:
                a[nr][nc] = a[r][c] + 1
                q.append((nr, nc))

    return a
