> LeetCode 0225. Implement Stack using Queues用队列实现栈【Easy】【Python】【栈】【队列】

### Problem

[LeetCode](https://leetcode.com/problems/implement-stack-using-queues/)

Implement the following operations of a stack using queues.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- empty() -- Return whether the stack is empty.

**Example:**

```
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
```

**Notes:**

- You must use *only* standard operations of a queue -- which means only `push to back`, `peek/pop from front`, `size`, and `is empty` operations are valid.
- Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
- You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

### 问题

[力扣](https://leetcode-cn.com/problems/implement-stack-using-queues/)

使用队列实现栈的下列操作：

* push(x) -- 元素 x 入栈
* pop() -- 移除栈顶元素
* top() -- 获取栈顶元素
* empty() -- 返回栈是否为空

**注意:**

* 你只能使用队列的基本操作-- 也就是 `push to back`, `peek/pop from front`, `size`, 和 `is empty` 这些操作是合法的。
* 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
* 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

### 思路

**栈**  **队列**

```
数据结构基础
```

##### Python3代码

```python
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myStack = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.myStack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # judge if it is empty
        if not self.empty():
            return self.myStack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        # judge if it is empty
        if not self.empty():
            return self.myStack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.myStack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0225-Implement-Stack-using-Queues/0225.py)