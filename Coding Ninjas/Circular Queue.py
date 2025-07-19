# from os import *
# from sys import *
# from collections import *
# from math import *

class CircularQueue:
    def __init__(self, n):
        # Initialize your data structure.
        self.size = n
        self.queue = [None] * n 
        self.front = -1
        self.rear = -1

    # Enqueues 'X' into the queue. Returns true if it gets pushed into the queue, and false otherwise.
    def enqueue(self, value):
        # Write your code here.
        if (self.rear + 1) % self.size == self.front:
            return False

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        
        self.queue[self.rear] = value
        return True

    # Dequeues pop element from queue. Returns -1 if the queue is empty, otherwise returns the popped element.
    def dequeue(self):
        # Write your code here.
        if self.front == -1:
            return -1
        
        val = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return val
