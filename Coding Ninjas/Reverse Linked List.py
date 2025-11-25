'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def reverseLinkedList(head):
    prev = None
    curr = head
    
    while curr is not None:
        next_node = curr.next 
        curr.next = prev     
        
        prev = curr             
        curr = next_node       
    
    return prev
