> LeetCode 0680. Valid Palindrome II验证回文字符串 Ⅱ【Easy】【Python】【双指针】

### 题目

[英文题目链接](https://leetcode.com/problems/valid-palindrome-ii/)

Given a non-empty string `s`, you may delete **at most** one character. Judge whether you can make it a palindrome.

**Example 1:**

```
Input: "aba"
Output: True
```

**Example 2:**

```
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
```

**Note:**

1. The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

### 翻译

[中文题目链接](https://leetcode-cn.com/problems/valid-palindrome-ii/submissions/)

给定一个非空字符串 s，**最多**删除一个字符。判断是否能成为回文字符串。

**示例 1:**

```
输入: "aba"
输出: True
```

**示例 2:**

```
输入: "abca"
输出: True
解释: 你可以删除c字符。
```

**注意:**

1. 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

### 思路

**双指针**

left 指针从头指向尾，right 指针从尾指向头。

* 如果 s[left] 和 s[right] 相等，left + 1，right - 1。

* 如果 s[left] 和 s[right] 不相等，分别删掉 s[left] 或者 s[right]，判断剩余的字符串是否满足回文，只要其中一个满足即可。

**时间复杂度**: O(n)

### Python代码

```python
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1  # 同时赋值
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                temp1 = s[:left] + s[left+1:]  # 删掉 s[left] 后的字符, 即字符串拼接: s[0] 到 s[left-1] + s[left+1] 到 s[len(s)-1]
                temp2 = s[:right] + s[right+1:]
                if temp1 == temp1[::-1] or temp2 == temp2[::-1]:  # 判断删掉 s[left] 或者删掉 s[right], s是否为回文, [::-1]是从尾到头逆序遍历
                    return True
                else:
                    return False
        return True
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0680-Valid-Palindrome-II/0680.py)