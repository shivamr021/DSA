from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

# Linked List Node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isPalindrome(head):
    if head is None or head.next is None:
        return True

    # Step 1: Find the middle node
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev, curr = None, slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second_half = prev  # new head of reversed half

    # Step 3: Compare both halves
    first_half = head
    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


# Helper function to create linked list from input
def takeinput():
    inputlist = [int(ele) for ele in input().split()]
    head = None
    tail = None

    for currentData in inputlist:
        if currentData == -1:
            break

        newNode = Node(currentData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head


# Main
t = int(stdin.readline().rstrip())
while t > 0:
    head = takeinput()
    if isPalindrome(head):
        print('true')
    else:
        print('false')
    t -= 1
