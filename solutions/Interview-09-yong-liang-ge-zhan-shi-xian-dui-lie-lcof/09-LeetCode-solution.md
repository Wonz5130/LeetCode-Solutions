> LeetCode 面试题09. 用两个栈实现队列【剑指Offer】【Easy】【Python】【栈】【队列】

### 问题

[力扣](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

**示例 1：**

```
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
```

**示例 2：**

```
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
```

**提示：**

* `1 <= values <= 10000`
* `最多会对 appendTail、deleteHead 进行 10000 次调用`

### 思路

**栈 队列**

```
栈：先进后出
队列：先进先出

加入队尾：直接进栈 A

删除队首：主要是实现栈 A 的倒序
```

##### Python3代码

```python
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
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-09-yong-liang-ge-zhan-shi-xian-dui-lie-lcof/09.py)