> LeetCode 面试题59 - II. 队列的最大值【Medium】【Python】【队列】

### 问题

[力扣](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/)

请定义一个队列并实现函数 `max_value` 得到队列里的最大值，要求函数`max_value`、`push_back` 和 `pop_front` 的**均摊**时间复杂度都是O(1)。

若队列为空，`pop_front` 和 `max_value` 需要返回 -1

**示例 1：**

```
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
```

**示例 2：**

```
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
```

**限制：**

* `1 <= push_back,pop_front,max_value的总操作数 <= 10000`
* `1 <= value <= 10^5`

### 思路

**辅助队列**

```
sort_que 队列的头部永远是 que 队列的最大值。
```

**时间复杂度:** O(1)

##### Python3代码

```python
from collections import deque

class MaxQueue:

    def __init__(self):
        self.que = deque()
        self.sort_que = deque()

    def max_value(self) -> int:
        return self.sort_que[0] if self.sort_que else -1

    def push_back(self, value: int) -> None:
        self.que.append(value)
        # sort_que: non-increasing 非递增
        while self.sort_que and self.sort_que[-1] < value:
            self.sort_que.pop()
        self.sort_que.append(value)

    def pop_front(self) -> int:
        if not self.que:
            return -1
        res = self.que.popleft()  # popleft(): O(1), pop(i): O(n)
        if res == self.sort_que[0]:
            self.sort_que.popleft()
        return res

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-59-II/5902.py)

### 参考

[【Python】详解：为何添加辅助队列就能实现O(1)操作？](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/solution/python-xiang-jie-wei-he-tian-jia-fu-zhu-dui-lie-ji/)