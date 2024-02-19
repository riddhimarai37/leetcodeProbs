

class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.total_sum = 0
        self.queue = collections.deque()


    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            remove = self.queue.popleft()
            self.total_sum -= remove
        self.total_sum += val
        self.queue.append(val)
        return self.total_sum/len(self.queue)
            











# init 

        # self.queue = collections.deque()
        # self.size = size
        # self.curr_sum = 0






#next
        # avg = 0
        # if len(self.queue) < self.size:
        #     self.queue.append(val)
        #     self.curr_sum += val
        #     avg = self.curr_sum/len(self.queue)
        # else:
        #     self.curr_sum -= self.queue.popleft()
        #     self.queue.append(val)
        #     self.curr_sum += val
        #     avg = self.curr_sum/len(self.queue)
        # return avg

            
            





        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


# from collectionsn import dequeue
# init
        # self.length = 0
        # self.max = size
        # self.sum = 0
        # self.queue = deque()

# next 
        # if self.length < self.max:
        #     self.length +=1
        #     self.queue.append(val)
        #     self.sum += val
        # else:
        #     self.sum -= self.queue.popleft()
        #     self.queue.append(val)
        #     self.sum += val
        # return self.sum/self.length
