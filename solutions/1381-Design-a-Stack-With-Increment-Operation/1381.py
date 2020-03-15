class CustomStack:

    def __init__(self, maxSize: int):
        self.size = 0
        self.maxSize = maxSize
        self.customStack = []

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.customStack.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        temp = self.customStack[self.size - 1]
        # 要把栈顶元素弹出去，即删除栈顶元素
        del self.customStack[self.size - 1]
        self.size -= 1
        return temp

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.size)):
            self.customStack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)