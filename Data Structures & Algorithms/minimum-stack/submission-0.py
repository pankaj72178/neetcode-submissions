class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        if (len(self.stack) == 0):
            self.stack.append(val)
            self.minstack.append(val)
        else:
            self.stack.append(val)
            val1 = self.minstack.pop()
            self.minstack.append(val1)
            self.minstack.append(min(val,val1))
        

    def pop(self) -> None:
        if (len(self.stack) == 0):
            return False
        val = self.stack.pop()
        self.minstack.pop()
        return val
        

    def top(self) -> int:
        if (len(self.stack) == 0):
            return False

        val = self.stack.pop()
        self.stack.append(val)
        return val
        

    def getMin(self) -> int:
        if (len(self.stack) == 0):
            return False
        
        val = self.minstack.pop()
        self.minstack.append(val)
        return val
