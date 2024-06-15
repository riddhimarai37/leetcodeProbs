class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        if not self.stack1:
            self.stack1.append(x)
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

            self.stack1.append(x)
            while self.stack2:
                self.stack1.append(self.stack2.pop())

        print(self.stack1)
            

    def pop(self) -> int:
        ret = self.stack1.pop()
        return ret
        

    def peek(self) -> int:
        ret = self.stack1.pop()
        self.stack1.append(ret)
        return ret
        

    def empty(self) -> bool:
        if self.stack1 or self.stack2:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()