from typing import List
from collections import deque
def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
    # write your code here
    visited = [False] * n
    queue = deque()
    bfs = []

    queue.append(0)
    visited[0] = True

    while queue:
        node = queue.popleft()
        bfs.append(node)

        for nei in adj[node]:
            if not visited[nei]:
                queue.append(nei)
                visited[nei] = True

    return bfs
