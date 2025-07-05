# from os import *
# from sys import *
# from collections import *
# from math import *


# Following is the linked list node structure:

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

from typing import *

def merge(heads: List[Node]) -> None:
    # Write your code here.
    h1, h2 = heads
    while h1 or h2:
        h1_next = h1.next
        h2_next = h2.next

        h1.next = h2
        h2.next = h1_next

        h1 = h1_next
        h2 = h2_next

    heads[1] = h2
