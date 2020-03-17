> LeetCode 面试题05. 替换空格【剑指Offer】【Easy】【Python】【字符串】

### 问题

[力扣](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

**示例 1：**

```
输入：s = "We are happy."
输出："We%20are%20happy."
```

**限制：**

`0 <= s 的长度 <= 10000`

### 思路

##### 解法一

**字符串遍历**

**时间复杂度:** O(n)，n 为字符串长度。

##### Python3代码

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        # solution one
        res = ''
        for c in s:
            if c == ' ':
                res += '%20'
            else:
                res += c
        return res
```

##### 解法二

**字符串遍历**

**时间复杂度:** O(n)，n 为字符串长度。

##### Python3代码

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        # solution two
        return ''.join(('%20' if c ==' ' else c for c in s))
```

##### 解法三

**replace函数**

##### Python3代码

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        # solution three
        return s.replace(' ', '%20')
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-05-ti-huan-kong-ge-lcof/05.py)