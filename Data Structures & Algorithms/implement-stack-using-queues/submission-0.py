class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        if (len(self.queue1) == 0 and len(self.queue2) == 0):
            self.queue1.append(x)

        elif (len(self.queue1) == 0):
            self.queue2.append(x)
        
        else:
            self.queue1.append(x)
            

    def pop(self) -> int:
        if (len(self.queue1) == 0 and len(self.queue2) == 0):
            return -1
        
        if (len(self.queue1) == 0):
            self.queue1 = self.queue2
            self.queue2 = []
        
        val = self.queue1.pop(0)
        while self.queue1:
            self.queue2.append(val)
            val = self.queue1.pop(0)
        
        return val

        

    def top(self) -> int:
        if (len(self.queue1) == 0 and len(self.queue2) == 0):
            return -1
        
        if (len(self.queue1) == 0):
            self.queue1 = self.queue2
            self.queue2 = []
        
        val = self.queue1.pop(0)
        while self.queue1:
            self.queue2.append(val)
            val = self.queue1.pop(0)
        
        self.queue2.append(val)
        
        return val     


    def empty(self) -> bool:
        if (len(self.queue1) == 0 and len(self.queue2) == 0):
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()