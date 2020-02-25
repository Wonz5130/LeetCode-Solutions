> LeetCode 0241. Different Ways to Add Parentheses为运算表达式设计优先级【Medium】【Python】【分治】

### Problem

[LeetCode](https://leetcode.com/problems/different-ways-to-add-parentheses/)

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are `+`, `-` and `*`.

**Example 1:**

```
Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
```

**Example 2:**

```
Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
```

### 问题

[力扣](https://leetcode-cn.com/problems/different-ways-to-add-parentheses/)

给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含  `+`, `-` 和 `*` 。

**示例 1:**

```
输入: "2-1-1"
输出: [0, 2]
解释: 
((2-1)-1) = 0 
(2-(1-1)) = 2
```

**示例 2:**

```
输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
```

### 思路

**分治**

```
循环遍历，如果当前位置是运算符，那么分别计算左右两边的式子的值，然后用运算符拼接在一起。
```

**时间复杂度:** O(n)

### Python3代码

```python
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # solution: Divide and conquer
        if input.isdigit():  # input only contains digital
            return [int(input)]
        n = len(input)
        res = []
        for i in range(n):
            if input[i] in '+-*':
                lefts = self.diffWaysToCompute(input[:i])
                rights = self.diffWaysToCompute(input[i+1:])
                for left in lefts:
                    for right in rights:
                        if input[i] == '+':
                            res.append(left + right)
                        elif input[i] == '-':
                            res.append(left - right)
                        elif input[i] == '*':
                            res.append(left * right)
                        # # use eval
                        # res.append(eval(str(left) + input[i] + str(right)))
        return res
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0241-Different-Ways-to-Add-Parentheses/0241.py)