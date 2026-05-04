class MinStack:

    def __init__(self):
        self.stack = []
        self.minst = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minst[-1] if self.minst else val)
        self.minst.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minst.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minst[-1]
        
