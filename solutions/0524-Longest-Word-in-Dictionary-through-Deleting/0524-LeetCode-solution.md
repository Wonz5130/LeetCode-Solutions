> LeetCode 0524. Longest Word in Dictionary through Deleting通过删除字母匹配到字典里最长单词【Medium】【Python】【双指针】

### 题目

[英文题目地址](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/)

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

**Example 1:**

```
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
```

**Example 2:**

```
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
```

**Note:**

1. All the strings in the input will only contain lower-case letters.
2. The size of the dictionary won't exceed 1,000.
3. The length of all the strings in the input won't exceed 1,000.

### 翻译

[中文题目地址](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/)

给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

**示例 1:**

```
输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

输出: 
"apple"
```

**示例 2:**

```
输入:
s = "abpcplea", d = ["a","b","c"]

输出: 
"a"
```

**说明:**

1. 所有输入的字符串只包含小写字母。
2. 字典的大小不会超过 1000。
3. 所有输入的字符串长度不会超过 1000。

### 思路

**双指针**

i 指针在 s 字符串中移动，j 指针在 d 字典中的每个字符串中移动。如果不同，则只移动 j 指针，如果 j 指针能移到字符串末尾，说明此字符串是在 s 中的，比较此时的字符串长度 len 是否大于之前存的 len，若大于则更新，若等于，则取最小字典序。

**空间复杂度**: O(1)

### Python代码

```python
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        res = ""
        max = -1
        for word in d:
            if len(s) < len(word) or len(word) == 0:
                continue
            j = 0  # j 指针判断 word 中的每个字符
            for i in range(len(s)):  # i 指针判断 s 中的每个字符
                if s[i] == word[j]:
                    j += 1  # 如果相等, 只移动 j 指针
                if j == len(word):  # j 指针已移动 word 末尾
                    if len(word) > max:  # 更新 res 和 max
                        res = word
                        max = len(word)
                    elif len(word) == max:
                        res = min(res, word)  # 长度相同选最小字典序的 word 
                    break
        return res
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0524-Longest-Word-in-Dictionary-through-Deleting/0524.py)