> LeetCode 1408. String Matching in an Array数组中的字符串匹配【Easy】【Python】【字符串】

### Problem

[LeetCode](https://leetcode.com/problems/string-matching-in-an-array/)

Given an array of string `words`. Return all strings in `words` which is substring of another word in **any** order. 

String `words[i]` is substring of `words[j]`, if can be obtained removing some characters to left and/or right side of `words[j]`.

**Example 1:**

```
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
```

**Example 2:**

```
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
```

**Example 3:**

```
Input: words = ["blue","green","bu"]
Output: []
```

**Constraints:**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 30`
- `words[i]` contains only lowercase English letters.
- It's **guaranteed** that `words[i]` will be unique.

### 问题

[力扣](https://leetcode-cn.com/problems/string-matching-in-an-array/)

给你一个字符串数组 words ，数组中的每个字符串都可以看作是一个单词。请你按 任意 顺序返回 words 中是其他单词的子字符串的所有单词。

如果你可以删除 words[j] 最左侧和/或最右侧的若干字符得到 word[i] ，那么字符串 words[i] 就是 words[j] 的一个子字符串。

**示例 1：**

```
输入：words = ["mass","as","hero","superhero"]
输出：["as","hero"]
解释："as" 是 "mass" 的子字符串，"hero" 是 "superhero" 的子字符串。
["hero","as"] 也是有效的答案。
```

**示例 2：**

```
输入：words = ["leetcode","et","code"]
输出：["et","code"]
解释："et" 和 "code" 都是 "leetcode" 的子字符串。
```

**示例 3：**

```
输入：words = ["blue","green","bu"]
输出：[]
```


**提示：**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 30`
- words[i] 仅包含小写英文字母。
- 题目数据 保证 每个 words[i] 都是独一无二的。

### 思路

**字符串**

```
暴力，最后要去重。
```

**时间复杂度:** O(n^2)
**空间复杂度:** O(n)

##### Python3代码

```python
from typing import List
import copy

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        res = []
        for i in range(n):
            temp = copy.deepcopy(words)
            temp.remove(words[i])

            for j in range(n - 1):
                if words[i] in temp[j]:
                    res.append(words[i])
        return list(set(res))
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1408-String-Matching-in-an-Array/1408.py)