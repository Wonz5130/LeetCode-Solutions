> LeetCode 1381. Design a Stack With Increment Operation设计一个支持增量操作的栈【Medium】【Python】【栈】

### Problem

[LeetCode](https://leetcode.com/problems/design-a-stack-with-increment-operation/)

Design a stack which supports the following operations.

Implement the `CustomStack` class:

- `CustomStack(int maxSize)` Initializes the object with `maxSize` which is the maximum number of elements in the stack or do nothing if the stack reached the `maxSize`.
- `void push(int x)` Adds `x` to the top of the stack if the stack hasn't reached the `maxSize`.
- `int pop()` Pops and returns the top of stack or **-1** if the stack is empty.
- `void inc(int k, int val)` Increments the bottom `k` elements of the stack by `val`. If there are less than `k` elements in the stack, just increment all the elements in the stack.

**Example 1:**

```
Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack customStack = new CustomStack(3); // Stack is Empty []
customStack.push(1);                          // stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.push(3);                          // stack becomes [1, 2, 3]
customStack.push(4);                          // stack still [1, 2, 3], Don't add another elements as size is 4
customStack.increment(5, 100);                // stack becomes [101, 102, 103]
customStack.increment(2, 100);                // stack becomes [201, 202, 103]
customStack.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
customStack.pop();                            // return 202 --> Return top of the stack 102, stack becomes [201]
customStack.pop();                            // return 201 --> Return top of the stack 101, stack becomes []
customStack.pop();                            // return -1 --> Stack is empty return -1.
```

**Constraints:**

- `1 <= maxSize <= 1000`
- `1 <= x <= 1000`
- `1 <= k <= 1000`
- `0 <= val <= 100`
- At most `1000` calls will be made to each method of `increment`, `push` and `pop` each separately.

### 问题

[力扣](https://leetcode-cn.com/problems/design-a-stack-with-increment-operation/)

请你设计一个支持下述操作的栈。

实现自定义栈类 CustomStack ：

- CustomStack(int maxSize)：用 maxSize 初始化对象，maxSize 是栈中最多能容纳的元素数量，栈在增长到 maxSize 之后则不支持 push 操作。
- void push(int x)：如果栈还未增长到 maxSize ，就将 x 添加到栈顶。
- int pop()：返回栈顶的值，或栈为空时返回 -1 。
- void inc(int k, int val)：栈底的 k 个元素的值都增加 val 。如果栈中元素总数小于 k ，则栈中的所有元素都增加 val 。

**示例：**

```
输入：
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
输出：
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
解释：
CustomStack customStack = new CustomStack(3); // 栈是空的 []
customStack.push(1);                          // 栈变为 [1]
customStack.push(2);                          // 栈变为 [1, 2]
customStack.pop();                            // 返回 2 --> 返回栈顶值 2，栈变为 [1]
customStack.push(2);                          // 栈变为 [1, 2]
customStack.push(3);                          // 栈变为 [1, 2, 3]
customStack.push(4);                          // 栈仍然是 [1, 2, 3]，不能添加其他元素使栈大小变为 4
customStack.increment(5, 100);                // 栈变为 [101, 102, 103]
customStack.increment(2, 100);                // 栈变为 [201, 202, 103]
customStack.pop();                            // 返回 103 --> 返回栈顶值 103，栈变为 [201, 202]
customStack.pop();                            // 返回 202 --> 返回栈顶值 202，栈变为 [201]
customStack.pop();                            // 返回 201 --> 返回栈顶值 201，栈变为 []
customStack.pop();                            // 返回 -1 --> 栈为空，返回 -1
```

**提示：**

- `1 <= maxSize <= 1000`
- `1 <= x <= 1000`
- `1 <= k <= 1000`
- `0 <= val <= 100`
- 每种方法 `increment`，`push` 以及 `pop` 分别最多调用 `1000` 次

### 思路

**栈**

```
这里我犯了个错，pop 时记得要把栈顶元素弹出，不能只是返回，一定要弹出。
```

##### Python3代码

```python
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
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1381-Design-a-Stack-With-Increment-Operation/1381.py)