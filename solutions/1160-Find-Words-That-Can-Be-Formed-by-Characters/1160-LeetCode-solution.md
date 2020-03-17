> LeetCode 1160. Find Words That Can Be Formed by Characters拼写单词【Easy】【Python】【字符串】

### Problem

[LeetCode](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/)

You are given an array of strings `words` and a string `chars`.

A string is *good* if it can be formed by characters from `chars` (each character can only be used once).

Return the sum of lengths of all good strings in `words`.

**Example 1:**

```
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
```

**Example 2:**

```
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
```

**Note:**

1. `1 <= words.length <= 1000`
2. `1 <= words[i].length, chars.length <= 100`
3. All strings contain lowercase English letters only.

### 问题

[力扣](https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/)

给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。

假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写时，chars 中的每个字母都只能用一次。

返回词汇表 words 中你掌握的所有单词的 **长度之和**。

**示例 1：**

```
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释： 
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
```

**示例 2：**

```
输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
输出：10
解释：
可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
```

**提示：**

1. `1 <= words.length <= 1000`
2. `1 <= words[i].length, chars.length <= 100`
3. 所有字符串中都仅包含小写英文字母

### 思路

**字符串**

##### 解法一

```
用 collections，代码风格比较 pythonic。
```

##### Python3代码

```python
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # solution one
        import collections
        res = 0
        cnt = collections.Counter(chars)
        for word in words:
            c = collections.Counter(word)
            if all([c[i] <= cnt[i] for i in c]):
                res += len(word)
        return res
```

##### 解法二

```
判断 word 中各个字符个数是否 <= chars 中这些字符个数。
```

##### Python3代码

```python
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # solution two
        res = 0
        for word in words:
            n = len(word)
            cnt = 0
            for i in word:
                # word 中字符 i 个数 <= chars 中字符 i 个数
                if word.count(i) <= chars.count(i):
                    cnt += 1
                else:
                    break
            # word 可以由 chars 拼出
            if cnt == n:
                res += cnt
        return res
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1160-Find-Words-That-Can-Be-Formed-by-Characters/1160.py)