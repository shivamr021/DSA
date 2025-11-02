def countDistinctSubstrings(s):
    # Write your code here
    class TrieNode:
        def __init__(self):
            self.children = {}
        
    root = TrieNode()
    cnt = 0

    for i in range(len(s)):
        node = root
        for j in range(i, len(s)):
            ch = s[j]
            if ch not in node.children:
                node.children[ch] = TrieNode()
                cnt += 1
            node = node.children[ch]
    
    return cnt + 1
