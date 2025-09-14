from os import *
from sys import *
from collections import *
from math import *
  
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


def insert(k, val, head):
    # Write your code here.
    newNode = Node(val)

    if k == 0:
        newNode.next = head
        if head:
            head.prev = newNode
        return newNode

    curr = head
    for _ in range(k-1):
        curr = curr.next

    newNode.next = curr.next
    newNode.prev = curr

    if curr.next:
        curr.next.prev = newNode

    curr.next = newNode

    return head
