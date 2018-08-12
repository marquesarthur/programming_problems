class MinStack:
    def __init__(self):
        self.stack = []

    # @param x, an integer
    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            y, _min = self.stack[-1]
            self.stack.append((x, min(x, _min)))

    # @return nothing
    def pop(self):
        if self.stack:
            self.stack = self.stack.pop()

    # @return an integer
    def top(self):
        if self.stack:
            value, _min = self.stack[-1]
            return value
        return -1

    # @return an integer
    def getMin(self):
        if self.stack:
            value, _min = self.stack[-1]
            return _min
        return -1

