> LeetCode 0509. Fibonacci Number斐波那契数【Easy】【Python】【动态规划】

### Problem

[LeetCode](https://leetcode.com/problems/fibonacci-number/)

The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,

```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
```

Given `N`, calculate `F(N)`.

**Example 1:**

```
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

**Example 2:**

```
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```

**Example 3:**

```
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

**Note:**

0 ≤ `N` ≤ 30.

### 问题

[力扣](https://leetcode-cn.com/problems/fibonacci-number/)

**斐波那契数**，通常用 F(n) 表示，形成的序列称为**斐波那契数列**。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
```


给定 N，计算 F(N)。

 **示例 1：**

```
输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
```

**示例 2：**

```
输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
```

**示例 3：**

```
输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
```

**提示：**

* `0 ≤ N ≤ 30`

### 思路

##### 解法一：递归

```
fib(n) = fib(n - 1) + fib(n - 2)
注意，fib(n)会越界，所以最好是：
fib(n) % 1000000007 = (fib(n - 1) % 1000000007 + fib(n - 2) % 1000000007) % 1000000007
但是因为 Python 中整形数字的大小限制取决计算机的内存（可理解为无限大），因此可不考虑大数越界问题。
```

##### Python3代码

```python
class Solution:
    def fib(self, n: int) -> int:
        # solution one: 递归
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
```

##### 解法二：动态规划

**时间复杂度:** O(n)
**空间复杂度:** O(1)

##### Python3代码

```python
class Solution:
    def fib(self, n: int) -> int:
        # solution two: 动态规划
        dp_0, dp_1 = 0, 1
        for _ in range(n):
            dp_0, dp_1 = dp_1, dp_0 + dp_1
        return dp_0
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0509-Fibonacci-Number/0509.py)