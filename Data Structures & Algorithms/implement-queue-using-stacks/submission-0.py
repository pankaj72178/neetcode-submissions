class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack2.append(x)
        

    def pop(self) -> int:
        if(len(self.stack2) == 0):
            return False
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())
        val = self.stack1.pop()
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        return val
        

    def peek(self) -> int:
        if(len(self.stack2) == 0):
            return False
        val = 0
        while len(self.stack2):
            val = self.stack2.pop()
            self.stack1.append(val)
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        return val
        

    def empty(self) -> bool:
        return len(self.stack2)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()