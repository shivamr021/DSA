from collections import defaultdict, OrderedDict

class Node:
    def __init__(self, key, val, freq=1):
        self.key = key
        self.val = val
        self.freq = freq

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_table = {}
        self.freq_table = defaultdict(OrderedDict)
        self.min_freq = 0

    def _update_freq(self, node: Node):
        freq = node.freq
        del self.freq_table[freq][node.key]
        if not self.freq_table[freq]:
            del self.freq_table[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        node.freq += 1
        self.freq_table[node.freq][node.key] = node

    def get(self, key: int) -> int:
        if key not in self.key_table:
            return -1

        node = self.key_table[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_table:
            node = self.key_table[key]
            node.val = value
            self._update_freq(node)
        else:
            if len(self.key_table) == self.capacity:
                k, v = self.freq_table[self.min_freq].popitem(last=False)
                del self.key_table[k]

            new_node = Node(key, value)
            self.key_table[key] = new_node
            self.freq_table[1][key] = new_node
            self.min_freq = 1
