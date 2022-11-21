> LeetCode 面试题10- I. 斐波那契数列【剑指Offer】【Easy】【动态规划】【快速幂】

# 问题

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

# 方法一：动态规划

```
fib(n) = fib(n - 1) + fib(n - 2)
注意，fib(n)会越界，所以最好是：
fib(n) % 1000000007 = (fib(n - 1) % 1000000007 + fib(n - 2) % 1000000007) % 1000000007
但是因为 Python 中整形数字的大小限制取决计算机的内存（可理解为无限大），因此可不考虑大数越界问题。
```

**时间复杂度:** O(n)
**空间复杂度:** O(1)

## Python3

```python
class Solution:
    def fib(self, n: int) -> int:
        dp_0, dp_1 = 0, 1
        for _ in range(n):
            dp_0, dp_1 = dp_1, dp_0 + dp_1
        return dp_0 % 1000000007
```

## Go

```go
func fib(n int) int {
    var mod int = 1e9 + 7
    if n < 2 {
        return n
    }
    p, q, sum := 0, 0, 1
    for i := 2; i <= n; i++ {
        p = q
        q = sum
        sum = (p + q) % mod
    }
    return sum 
}
```

# 方法二：快速幂

与运算&：两个二进制位的值同时为1，结果为1，否则为0

或运算|：两个二进制位，一个值为1，其值为1

异或运算^：两个二进制位的值不同，则该位结果为1，否则为0

## Python3

```python
class Solution:
    def fib(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 2:
            return n
        
        def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            c = [[0, 0], [0, 0]]
            for i in range (2):
                for j in range(2):
                    c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % MOD
            return c
        
        def matrix_pow(a: List[List[int]], n: int) -> List[List[int]]:
            base = [[1, 0], [0, 1]]
            while n > 0:
                if n & 1:
                    base = multiply(base, a)
                n >>= 1
                a = multiply(a, a)
            return base
        
        res = matrix_pow([[1, 1], [1, 0]], n - 1)
        return res[0][0]
```

# 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-10-fei-bo-na-qi-shu-lie-lcof/10-1.py)