from os import *
from sys import *
from collections import *
from math import *

class Queue:
    # Stacks to be used in the operations.
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    # Enqueues 'X' into the queue. Returns true after enqueuing.
    def enqueue(self, X):
        # Write your code here
        self.stk1.append(X)
        return True

    """
      Dequeues top element from queue. Returns -1 if the queue is empty, 
      otherwise returns the popped element.
    """
    def dequeue(self):
        # Write your code here
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
        if not self.stk2:
            return -1
        return self.stk2.pop()
