class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
            
        q = deque([(root, 0)])
        hd_to_val = {} # hd = Horizontal Distance
        
        while q:
            node, hd = q.popleft()
            hd_to_val[hd] = node.data
            
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
                
        return [hd_to_val[hd] for hd in sorted(hd_to_val)]
