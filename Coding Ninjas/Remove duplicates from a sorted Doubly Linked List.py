class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def removeDuplicates(head: Node) -> Node:
    # Write your code here
    if not head:
        return None
    
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            dup = curr.next
            curr.next = dup.next
            if dup.next:
                dup.next.prev = curr
        else:
            curr = curr.next

    return head
