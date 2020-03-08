> LeetCode 1374. Generate a String With Characters That Have Odd Counts生成每种字符都是奇数个的字符串【Easy】【Python】【字符串】

### Problem

[LeetCode](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/)

Given an integer `n`, *return a string with `n` characters such that each character in such string occurs **an odd number of times***.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return **any** of them.  

**Example 1:**

```
Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
```

**Example 2:**

```
Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
```

**Example 3:**

```
Input: n = 7
Output: "holasss"
```

**Constraints:**

- `1 <= n <= 500`

### 问题

[力扣](https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts/)

给你一个整数 n，请你返回一个含 n 个字符的字符串，其中每种字符在该字符串中都恰好出现 **奇数次** 。

返回的字符串必须只含小写英文字母。如果存在多个满足题目要求的字符串，则返回其中任意一个即可。

**示例 1：**

```
输入：n = 4
输出："pppz"
解释："pppz" 是一个满足题目要求的字符串，因为 'p' 出现 3 次，且 'z' 出现 1 次。当然，还有很多其他字符串也满足题目要求，比如："ohhh" 和 "love"。
```

**示例 2：**

```
输入：n = 2
输出："xy"
解释："xy" 是一个满足题目要求的字符串，因为 'x' 和 'y' 各出现 1 次。当然，还有很多其他字符串也满足题目要求，比如："ag" 和 "ur"。
```

**示例 3：**

```
输入：n = 7
输出："holasss"
```

**提示：**

* `1 <= n <= 500`

### 思路

**字符串**

```
n 为偶数，n-1 个 'a' + 1 个 'b'
n 为奇数，n 个 'a'
```

**时间复杂度:** O(n)
**空间复杂度:** O(n)

##### Python3代码

```python
class Solution:
    def generateTheString(self, n: int) -> str:
        res = []
        if n % 2 == 0:
            for i in range(n-1):
                res.append('a')
            res.append('b')
        else:
            for i in range(n):
                res.append('a')
        return ''.join(res)
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1374-Generate-a-String-With-Characters-That-Have-Odd-Counts/1374.py)