class MinStack:


    def __init__(self):
        self.stack = []
        self.minVal = []
    def push(self, val):
        self.stack.append(val)
        if self.minVal == []:
            self.minVal.append(val)
        else:
            self.minVal.append(min(val, self.minVal[-1]))

    def pop(self):
        self.stack.pop()
        self.minVal.pop()

    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.minVal[-1]