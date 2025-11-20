from typing import List

def depthFirstSearch(V: int, E: int, edges: List[List[int]]):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    for x in adj:
        x.sort()

    visited = [False] * V
    components = []

    def dfs(node, comp):
        visited[node] = True
        comp.append(node)
        for neigh in adj[node]:
            if not visited[neigh]:
                dfs(neigh, comp)

    for i in range(V):
        if not visited[i]:
            comp = []
            dfs(i, comp)
            comp.sort()    
            components.append(comp)

    return components
