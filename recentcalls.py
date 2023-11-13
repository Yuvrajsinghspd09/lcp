from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Add the current timestamp to the queue
        self.requests.append(t)

        # Remove timestamps older than 3000 milliseconds
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        # Return the number of recent requests
        return len(self.requests)
