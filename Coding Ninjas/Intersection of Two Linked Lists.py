class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findIntersection(firstHead, secondHead):
    if not firstHead or not secondHead:
        return None

    a, b = firstHead, secondHead

    # Traverse until they meet or both become None
    while a != b:
        a = a.next if a else secondHead
        b = b.next if b else firstHead

    # Either intersection node or None
    return a
