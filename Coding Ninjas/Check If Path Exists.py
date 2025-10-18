from collections import deque

def checkPathExists(v, e, source, destination, edges):
    # Build adjacency list
    graph = [[] for _ in range(v)]
    for u, w in edges:
        graph[u].append(w)
    
    # BFS traversal
    q = deque([source])
    visited = [False] * v
    visited[source] = True
    
    while q:
        node = q.popleft()
        if node == destination:
            return True
        
        for nei in graph[node]:
            if not visited[nei]:
                visited[nei] = True
                q.append(nei)
    
    return False
