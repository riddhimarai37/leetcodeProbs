class MyQueue:

    def __init__(self):
        self.add_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
		# When we add to the queue, we want to add to the addStack
		# if we previously popped, we want to move all items from the popStack to the addStack
        while self.pop_stack:
            self.add_stack.append(self.pop_stack.pop())

        self.add_stack.append(x)

    def pop(self) -> int:
        while self.add_stack:
            self.pop_stack.append(self.add_stack.pop())
        return self.pop_stack.pop()


    def peek(self) -> int:
        if self.pop_stack:
            return self.pop_stack[-1]
        return self.add_stack[0]
        

    def empty(self) -> bool:
        if not self.pop_stack and not self.add_stack:
            return True
        return False

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()