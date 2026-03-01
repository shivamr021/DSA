from typing import Optional

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

def oddEvenList(head: Optional[Node]) -> Optional[Node]:
    # Write your code here.
    if not head or not head.next:
        return head
    
    odd = head
    even = head.next
    evenHead = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next
    
    odd.next = evenHead

    return head
