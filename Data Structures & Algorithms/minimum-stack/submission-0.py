class MinStack:
    def __init__(self):
        self.stack = []
        self.min_indices = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # case removing min where to set new min?
        if len(self.min_indices) == 0:
            self.min_indices.append(val)
        elif self.min_indices[-1] > val:
            self.min_indices.append(val)
        else:
            self.min_indices.append(self.min_indices[-1])

    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_indices.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int :
        return self.min_indices[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()