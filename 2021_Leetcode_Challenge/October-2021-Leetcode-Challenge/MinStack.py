class MinStack:
    def __init__(self):
        self.stack_main = []
        self.stack_min = []

    def push(self, x):
        self.stack_main.append(x)
        if not self.stack_min or self.stack_min[-1] >= x:
            self.stack_min.append(x)

    def pop(self):
        last = self.stack_main.pop()
        if last == self.stack_min[-1]:
            self.stack_min.pop()

    def top(self):
        return self.stack_main[-1]

    def getMin(self):
        return self.stack_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
