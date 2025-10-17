class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(node):
            for nei in range(n):
                if isConnected[node][nei] == 1 and not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        provinces = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                provinces += 1
        return provinces
