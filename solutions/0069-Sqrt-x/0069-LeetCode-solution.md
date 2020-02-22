> LeetCode 0069. Sqrt(x) x 的平方根【Easy】【Python】【二分】

### Problem

[LeetCode](https://leetcode.com/problems/sqrtx/)

Implement `int sqrt(int x)`.

Compute and return the square root of *x*, where *x* is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

**Example 1:**

```
Input: 4
Output: 2
```

**Example 2:**

```
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
```

### 问题

[力扣](https://leetcode-cn.com/problems/sqrtx/)

实现 `int sqrt(int x)` 函数。

计算并返回 *x* 的平方根，其中 *x* 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

**示例 1:**

```
输入: 4
输出: 2
```

**示例 2:**

```
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
```

### 思路

**法一:**
**二分查找**

```
典型的二分题目。注意返回值要是整数。
```

**法二:**
**牛顿迭代法**

详情可以看这篇文章：[牛顿迭代法快速寻找平方根](http://www.matrix67.com/blog/archives/361)。

```
令f(res) = res^2 - x，则sqrt(x)等价于求f(res)的根

初始假设答案 res = x

每一次迭代，令 res = (res + x / res) / 2

新的 res 值为当前 res 值对应的函数切线与 x 轴的交点横坐标，这就是牛顿迭代的本质。
```

**法三:**
直接用库函数。

**时间复杂度:** O(n)
**空间复杂度:** O(1)

### Python代码

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # solution one: binary search
        low, high, mid = 0, x, x / 2
        while low <= high:
            if mid ** 2 > x:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) / 2
        return int(mid)

        # # solution two: Newton's method
        # res = x
        # while res * res > x:
        #     res = (res + x / res) / 2
        # return int(res)

        # # solution three: math
        # import math
        # return int(math.sqrt(x))
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0069-Sqrt-x/0069.py)