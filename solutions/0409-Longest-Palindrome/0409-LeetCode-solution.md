> LeetCode 0409. Longest Palindrome最长回文串【Easy】【Python】【字符串】

### Problem

[LeetCode](https://leetcode.com/problems/longest-palindrome/)

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example `"Aa"` is not considered a palindrome here.

**Note:**
Assume the length of given string will not exceed 1,010.

**Example:**

```
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
```

### 问题

[力扣](https://leetcode-cn.com/problems/longest-palindrome/)

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 `"Aa"` 不能当做一个回文字符串。

**注意:**
假设字符串的长度不会超过 1010。

**示例 1:**

```
输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
```

### 思路

**字符串**

```
统计字符串中各个字符个数。
最后尽可能多地输出偶数个相同字符。
```

##### Python3代码

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        import collections
        # 统计各字符个数
        count = collections.Counter(s).values()
        sum = 0
        for x in count:
            if x // 2 > 0:
                # 取偶数个字符
                sum += x // 2 * 2
        if sum == len(s):
            return sum
        else:
            return sum + 1
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0409-Longest-Palindrome/0409.py)