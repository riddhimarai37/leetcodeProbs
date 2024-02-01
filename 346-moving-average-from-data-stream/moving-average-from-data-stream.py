# working solution but not optimized
# class MovingAverage:

#     def __init__(self, size: int):
#         self.stream = []
#         self.size = size
        
#     def next(self, val: int) -> float:
#         self.stream.append(val)
        
#         if len(self.stream) < self.size:
#             avg = 0
#             for x in self.stream:
#                 avg += x
#             avg /= len(self.stream)
#             return avg
#         else:
#             pt = len(self.stream)
#             avg = 0
#             for x in range(pt-self.size, pt):
#                 avg += self.stream[x]
#             avg /= self.size
#             return avg






# example: size = 2; next = 1 --> 1, next = 3 --> 4, next =5 --> 4


class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.size = size
        self.curr_sum = 0



    def next(self, val: int) -> float:
        avg = 0
        if len(self.queue) < self.size:
            self.queue.append(val)
            self.curr_sum += val
            avg = self.curr_sum/len(self.queue)
        else:
            self.curr_sum -= self.queue.popleft()
            self.queue.append(val)
            self.curr_sum += val
            avg = self.curr_sum/len(self.queue)
        return avg

            
            





        


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
