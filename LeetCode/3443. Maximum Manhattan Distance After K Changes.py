class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        from collections import Counter

        n = len(s)
        dirs = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

        prefix = [Counter()]
        for c in s:
            cnt = prefix[-1].copy()
            cnt[c] += 1
            prefix.append(cnt)

        max_dist = 0

        for i in range(n + 1):  
            cnt = prefix[i]
            dx = cnt['E'] - cnt['W']
            dy = cnt['N'] - cnt['S']
            base_dist = abs(dx) + abs(dy)

            
            bad_x = min(cnt['E'], cnt['W'])
            bad_y = min(cnt['N'], cnt['S'])

            max_flip = bad_x + bad_y
            flips = min(k, i)  
            max_gain = min(flips, max_flip) * 2
            max_dist = max(max_dist, base_dist + max_gain)

        return max_dist
