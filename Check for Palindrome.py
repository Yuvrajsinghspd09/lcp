from collections import deque

def reverse_queue(queue):
    reversed_queue = deque()

    while queue:
        reversed_queue.append(queue.pop())

    return reversed_queue

def palind_queue(queue):
    palind_queue = deque()


