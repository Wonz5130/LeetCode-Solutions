> LeetCode 面试题10- II. 青蛙跳台阶问题【剑指Offer】【Easy】【Python】【动态规划】

### 问题

[力扣](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

**示例 1：**

```
输入：n = 2
输出：2
```

**示例 2：**

```
输入：n = 7
输出：21
```

**提示：**

* `0 <= n <= 100`

注意：本题与主站 [70 题](https://leetcode-cn.com/problems/climbing-stairs/) 相同。

### 思路

**动态规划**

```
初始条件和斐波那契数列有点区别：dp_0 = 1，dp_1 = 1。

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
    def numWays(self, n: int) -> int:
        # 初始条件和斐波那契数列有区别
        dp_0, dp_1 = 1, 1
        for _ in range(n):
            dp_0, dp_1 = dp_1, dp_0 + dp_1
        return dp_0 % 1000000007
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-10-qing-wa-tiao-tai-jie-wen-ti-lcof/10-2.py)