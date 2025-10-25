from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        def dfs(node, comp_nodes):
            visited[node] = True
            comp_nodes.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, comp_nodes)            
        
        complete_cnt = 0

        for i in range(n):
            if not visited[i]:
                comp_nodes = []
                dfs(i, comp_nodes)

                edge_cnt = 0
                for node in comp_nodes:
                    edge_cnt += len(graph[node])
                edge_cnt //= 2

                k = len(comp_nodes)
                if edge_cnt == (k * (k-1)) // 2:
                    complete_cnt += 1
        return complete_cnt
