class MinStack:

    def __init__(self):
        self.Astack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.Astack.append(val)
        val = min(val, self.MinStack[-1]) if self.MinStack else val
        self.MinStack.append(val)
        
    def pop(self) -> None:
        self.Astack.pop()
        self.MinStack.pop()
        
        
    def top(self) -> int:
        return self.Astack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
        
val = [[],[-2],[0],[-3],[],[],[],[]]
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(val)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

