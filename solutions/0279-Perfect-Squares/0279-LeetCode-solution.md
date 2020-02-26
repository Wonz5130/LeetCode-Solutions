> LeetCode 0279. Perfect Squares完全平方数【Medium】【Python】【BFS】

### Problem

[LeetCode](https://leetcode.com/problems/perfect-squares/)

Given a positive integer *n*, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to *n*.

**Example 1:**

```
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
```

**Example 2:**

```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

### 问题

[力扣](https://leetcode-cn.com/problems/perfect-squares/)

给定正整数 *n*，找到若干个完全平方数（比如 `1, 4, 9, 16, ...`）使得它们的和等于 *n*。你需要让组成和的完全平方数的个数最少。

**示例 1:**

```
输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
```

**示例 2:**

```
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
```

### 思路

**解法一**

**BFS**

```
把每个整数都看成图中的节点，如果两个整数之差为一个平方数，表示两点之间存在一条边连通。
求最小平方数，就是求 n 到 0 的最短路径，于是就可以用 BFS。
```

**时间复杂度:** O(n^2)
**空间复杂度:** O(n^2)

### Python3代码

```python
class Solution:
    def numSquares(self, n: int) -> int:
        # solution one: BFS
        q = [(n, 0)]
        visited = [False for i in range(n + 1)]  # initialize all False
        visited[n] = True

        while any(q):  # any: if all elements are False, return False, or return True
            num, step = q.pop(0)

            i = 1
            Num = num - i ** 2
            while Num >= 0:
                if Num == 0:
                    return step + 1
                if not visited[Num]:  # not visited
                    q.append((Num, step + 1))
                    visited[Num] = True
                
                i += 1
                Num = num - i ** 2
```

**解法二**

**四平方和定理**

```
Lagrange 四平方定理：任何一个正整数都可以表示成不超过四个整数的平方之和。
于是答案只可能是：1，2，3，4。
还有一个定理：满足四数平方和定理的数 n（这里要满足由四个数构成，小于四个不行），必定满足 n=(8b+7)*4^a。
于是先缩小 n。
再判断，这个缩小后的数是否可以通过两个平方数的和或一个平方数组成，不能的话我们返回3，能的话我们返回平方数的个数。
```

### Python3代码

```python
class Solution:
    def numSquares(self, n: int) -> int:
        # solution two: Lagrange's Four-square Theorem
        while n % 4 == 0:  # reduce n
            n /= 4

        if n % 8 == 7:
            return 4

        a = 0
        while a ** 2 <= n:
            b = int((n - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == n:
                return (not not a) + (not not b)  # whether a and b are positive integers
            a += 1

        return 3
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0279-Perfect-Squares/0279.py)