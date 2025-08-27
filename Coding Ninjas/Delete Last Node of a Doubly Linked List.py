class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Do not change code above.


def deleteLastNode(head: Node) -> Node:
    # Write your code here
    if head is None:
        return
    
    if head.next is None:
        return None
    
    temp = head
    while temp.next:
        temp = temp.next
    
    temp.prev.next = None
    return head
