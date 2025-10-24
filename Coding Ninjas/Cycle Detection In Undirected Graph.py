from collections import defaultdict

def cycleDetection(edges, n, m):
    # Write your code here.
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)

    def dfs(node, parent):
        visited[node] = 1

        for nei in graph[node]:
            if not visited[nei]:
                if dfs(nei, node):
                    return True
            elif nei != parent:
                return True
        return False
      
    # Return "Yes" if cycle id present in the graph else return "No".
    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(i, -1):
                return "Yes"
    return "No"
