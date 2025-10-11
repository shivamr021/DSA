from collections import deque

def reverse(queue, k):
    stack = []

    for _ in range(k):
        stack.append(queue.popleft())
      
    while stack:
        queue.append(stack.pop())

    for _ in range(len(queue) - k):
        queue.append(queue.popleft())

    return queue
