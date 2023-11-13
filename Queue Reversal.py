from collections import deque

def rev_queue(orig_queue):
    rev_queue = deque()

    while orig_queue:
        rev_queue.append(orig_queue.pop())
    return rev_queue



orig_queue = [1,2,4,6,7,4,8,10,12,13]
rev_queue = rev_queue(orig_queue)
print("Original Queue:", list(orig_queue))
print("Reversed Queue:", list(rev_queue))
