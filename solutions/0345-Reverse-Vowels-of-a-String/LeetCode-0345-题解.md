> LeetCode 0345. Reverse Vowels of a String反转字符串中的元音字母【Easy】【Python】【双指针】

### 题目

[英文题目链接](https://leetcode.com/problems/reverse-vowels-of-a-string/)

Write a function that takes a string as input and reverse only the vowels of a string.

**Example 1:**

```
Input: "hello"
Output: "holle"
```

**Example 2:**

```
Input: "leetcode"
Output: "leotcede"
```

**Note:**
The vowels does not include the letter "y".

### 翻译

[中文题目链接](https://leetcode-cn.com/problems/reverse-vowels-of-a-string/)

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

**示例 1:**

```
输入: "hello"
输出: "holle"
```

**示例 2:**

```
输入: "leetcode"
输出: "leotcede"
```

**说明:**
元音字母不包含字母"y"。

### 思路

**双指针**

left 指针从左往右找 `元音字母` ，right 指针从右往左找 `元音字母` 。

考虑到字符串不能改变，因此需要用 `list` 来替代。

### Python代码

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, len(s)-1  # 同时赋值
        vowels = 'aeiou'
        string = list(s)  # 字符串不能改变, 所以要转为 list
        while left < right:
            if string[left].lower() not in vowels:  # lower 是取小写
                left += 1
            elif string[right].lower() not in vowels:
                right -= 1
            else:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
        return ''.join(string)  # 将 string 中的元素以指定的字符连接生成一个新的字符串
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0345-Reverse-Vowels-of-a-String/0345.py)

