> LeetCode 0365. Water and Jug Problem水壶问题【Medium】【Python】【BFS】【数学】

### Problem

[LeetCode](https://leetcode.com/problems/water-and-jug-problem/)

You are given two jugs with capacities *x* and *y* litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly *z* litres using these two jugs.

If *z* liters of water is measurable, you must have *z* liters of water contained within **one or both buckets** by the end.

Operations allowed:

- Fill any of the jugs completely with water.
- Empty any of the jugs.
- Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

**Example 1:** (From the famous [*"Die Hard"* example](https://www.youtube.com/watch?v=BVtQNK_ZUJg))

```
Input: x = 3, y = 5, z = 4
Output: True
```

**Example 2:**

```
Input: x = 2, y = 6, z = 5
Output: False
```

### 问题

[力扣](https://leetcode-cn.com/problems/water-and-jug-problem/)

有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

* 装满任意一个水壶
* 清空任意一个水壶
* 从一个水壶向另外一个水壶倒水，直到装满或者倒空

**示例 1:**  (From the famous "Die Hard" example)

```
输入: x = 3, y = 5, z = 4
输出: True
```

**示例 2:**

```
输入: x = 2, y = 6, z = 5
输出: False
```

### 思路

##### 解法一

**BFS**

```
每次水壶都有三个操作：加满水、清空水、相互倒。
```

##### Python3代码

```python
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # solution one: BFS
        from collections import deque
        queue = deque([[0, 0]])
        visited = set([(0, 0)])

        while queue:
            cur_x, cur_y = queue.pop()
            if z in [cur_x, cur_y, cur_x + cur_y]:
                return True
            for item in [
                # x 加满水，y 加满水
                (x, cur_y), (cur_x, y),
                # x 清空水，y 清空水
                (0, cur_y), (cur_x, 0),
                # 把 x 壶的水灌进 y 壶，直至灌满或倒空
                (cur_x + cur_y - y, y) if cur_x + cur_y >= y else (0, cur_x + cur_y),
                # 把 X 壶的水灌进 Y 壶，直至灌满或倒空
                (x, cur_x + cur_y - x) if cur_x + cur_y >= x else (cur_x + cur_y, 0)]:
                if item not in visited:
                    queue.appendleft(item)  # 从队列左边加入元素
                    visited.add(item)
        return False
```

##### 解法二

**裴蜀定理**

```
能否找到整数 a，b 使得方程 ax + by = z 有解。
有整数解时，当且仅当 z 是 a 和 b 的最大公约数 d 的倍数。
```

##### Python3代码

```python
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # solution two: 裴蜀定理
        import math
        if x + y < z:
            return False
        if x == z or y == z or x + y == z:
            return True
        return z % math.gcd(x, y) == 0
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0365-Water-and-Jug-Problem/0365.py)

### 参考

[暴力 + 数学](https://leetcode-cn.com/problems/water-and-jug-problem/solution/bao-li-shu-xue-by-powcai/)