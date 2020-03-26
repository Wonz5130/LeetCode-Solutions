class CQueue:

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        # B中还有倒序的元素，直接弹出
        if self.B:
            return self.B.pop()
        # A已空
        if not self.A:
            return -1
        # A中元素全部转到B中，实现倒序
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()