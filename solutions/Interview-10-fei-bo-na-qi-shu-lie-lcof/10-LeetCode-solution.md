> LeetCode 面试题10- I. 斐波那契数列【剑指Offer】【Easy】【Python】【动态规划】

### 问题

[力扣](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/)

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
```


斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

**示例 1：**

```
输入：n = 2
输出：1
```

**示例 2：**

```
输入：n = 5
输出：5
```

**提示：**

* `0 <= n <= 100`

注意：本题与主站 [509 题](https://leetcode-cn.com/problems/fibonacci-number/) 相同。

### 思路

**动态规划**

```
fib(n) = fib(n - 1) + fib(n - 2)
注意，fib(n)会越界，所以最好是：
fib(n) % 1000000007 = (fib(n - 1) % 1000000007 + fib(n - 2) % 1000000007) % 1000000007
但是因为 Python 中整形数字的大小限制取决计算机的内存（可理解为无限大），因此可不考虑大数越界问题。
```

**时间复杂度:** O(n)
**空间复杂度:** O(1)

##### Python3代码

```python
class Solution:
    def fib(self, n: int) -> int:
        dp_0, dp_1 = 0, 1
        for _ in range(n):
            dp_0, dp_1 = dp_1, dp_0 + dp_1
        return dp_0 % 1000000007
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-10-fei-bo-na-qi-shu-lie-lcof/10-1.py)