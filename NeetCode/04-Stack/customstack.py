class MinStack:

    def __init__(self):
        self.stack =[] 
        self.getminstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.getminstack[-1] if self.getminstack else val)
        self.getminstack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.getminstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.getminstack[-1]

