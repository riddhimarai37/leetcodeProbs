class RecentCounter:

    def __init__(self):
        self.counter = deque()


    def ping(self, t: int) -> int:
        self.counter.append(t)

        # Remove all ping in queue with value more than 3000 away from new ping
        while self.counter and self.counter[0] + 3000 < t:
            self.counter.popleft()

        return len(self.counter)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)