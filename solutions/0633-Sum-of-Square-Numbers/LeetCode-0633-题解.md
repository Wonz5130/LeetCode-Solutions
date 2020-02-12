> LeetCode 0633: Sum of Square Numbers平方数之和【Easy】【Python】

### 题目

[英文题目链接](https://leetcode.com/problems/sum-of-square-numbers/)

Given a non-negative integer `c`, your task is to decide whether there're two integers `a` and `b` such that a\*a  + b\*b = c.

**Example 1:**

```
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
```

**Example 2:**

```
Input: 3
Output: False
```

### 翻译

[中文题目链接](https://leetcode-cn.com/problems/sum-of-square-numbers/)

给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a\*a  + b\*b = c。

**示例1:**

```
输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5
```

**示例2:**

```
输入: 3
输出: False
```

### 思路

**双指针**

a 指针从 0 开始，b 指针取 c 的平方根。然后分别相向移动，如果 a\*a + b\*b < c，让 a 加 1，如果 a\*a + b\*b > c，让 b 减 1。

**时间复杂度**：
$$
O(\sqrt{c})
$$

### Python代码

```python
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        b = int(c**0.5)+1
        while a <= b:  # 假如 c = 2, 发现不加 = , 输出 False, 应该输出 True
            if a*a + b*b == c:
                return True
            elif a*a + b*b < c:
                a += 1
            else:
                b -= 1
        return False
```

### 本地测试版本代码

```python
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        b = int(c**0.5)+1
        while a <= b:  # 假如 c = 2, 发现不加 = , 输出 False, 应该输出 True
            if a*a + b*b == c:
                return True
            elif a*a + b*b < c:
                a += 1
            else:
                b -= 1
        return False

if __name__ == "__main__":
    c = 5
    print(Solution().judgeSquareSum(c))
```

