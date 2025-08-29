def stronglyConnectedComponents(v, edges):
    # Write your code here
    adj = [[] for _ in range(v)]
    for u, w in edges:
        adj[u].append(w)

    visited = [False] * v
    stack = []

    def dfs1(node):
        visited[node] = True
        for nei in adj[node]:
            if not visited[nei]:
                dfs1(nei)
        stack.append(node)

    for i in range(v):
        if not visited[i]:
            dfs1(i)

    rev_adj = [[] for _ in range(v)]
    for u in range(v):
        for w in adj[u]:
            rev_adj[w].append(u)
        
    
    visited = [False] * v

    def dfs2(node):
        visited[node] = True
        for nei in rev_adj[node]:
            if not visited[nei]:
                dfs2(nei)
    
    scc_count = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs2(node)
            scc_count += 1
    
    return scc_count
