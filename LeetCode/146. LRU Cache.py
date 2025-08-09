class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mpp = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insertAfterHead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def _deleteNode(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.mpp:
            return -1
        node = self.mpp[key]
        self._deleteNode(node)
        self._insertAfterHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mpp:
            node = self.mpp[key]
            node.val = value
            self._deleteNode(node)
            self._insertAfterHead(node)
        else:
            if len(self.mpp) == self.capacity:
                lru = self.tail.prev
                self._deleteNode(lru)
                del self.mpp[lru.key]
            new_node = Node(key, value)
            self.mpp[key] = new_node
            self._insertAfterHead(new_node)
