from collections import deque

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_map = {}
        start_node = None

        # Phase 1: Build parent pointers and locate start node
        def dfs(node, parent):
            nonlocal start_node
            if not node:
                return
            if node.val == start:
                start_node = node
            parent_map[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # Phase 2: BFS from start_node
        queue = deque([start_node])
        visited = set([start_node])
        minutes = -1 

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in (node.left, node.right, parent_map[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            minutes += 1

        return minutes
