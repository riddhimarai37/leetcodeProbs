class MovingAverage:

    def __init__(self, size: int):
        self.stream = []
        self.size = size
        
    def next(self, val: int) -> float:
        self.stream.append(val)
        
        if len(self.stream) < self.size:
            avg = 0
            for x in self.stream:
                avg += x
            avg /= len(self.stream)
            return avg
        else:
            pt = len(self.stream)
            avg = 0
            for x in range(pt-self.size, pt):
                avg += self.stream[x]
            avg /= self.size
            return avg



        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)