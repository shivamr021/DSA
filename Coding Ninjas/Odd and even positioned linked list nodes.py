from os import *
from sys import *
from collections import *
from math import *

'''
  ----- Linked list Node class for reference -----
        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None
            
'''

def oddEvenLinkedList(head):

    # Write your code.
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head
