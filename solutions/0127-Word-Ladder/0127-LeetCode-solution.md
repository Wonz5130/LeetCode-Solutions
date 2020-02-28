> LeetCode 0127. Word Ladder单词接龙【Medium】【Python】【BFS】

### Problem

[LeetCode](https://leetcode.com/problems/word-ladder/)

Given two words (*beginWord* and *endWord*), and a dictionary's word list, find the length of shortest transformation sequence from *beginWord* to *endWord*, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list. Note that *beginWord* is *not* a transformed word.

**Note:**

- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume *beginWord* and *endWord* are non-empty and are not the same.

**Example 1:**

```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
```

**Example 2:**

```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```

### 问题

[力扣](https://leetcode-cn.com/problems/word-ladder/)

给定两个单词（*beginWord* 和 *endWord*）和一个字典，找到从 *beginWord* 到 *endWord* 的最短转换序列的长度。转换需遵循如下规则：

1. 每次转换只能改变一个字母。
2. 转换过程中的中间单词必须是字典中的单词。

说明:

* 如果不存在这样的转换序列，返回 0。
* 所有单词具有相同的长度。
* 所有单词只由小写字母组成。
* 字典中不存在重复的单词。
* 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

**示例 1:**

```
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
```

**示例 2:**

```
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。
```

### 思路

##### 解法一

**BFS**

```
可以把单词每次转换改变一个字母看成是图的某条边，而两个单词就是两个顶点。
于是求最短转换序列的长度就是求最短路径，可以用 BFS。
把 26 个字母看成 26 个方向。
```

##### Python3代码

```Python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # solution one: BFS
        wordDict = set(wordList)  # no duplicates in the word list
        if endWord not in wordDict:
            return 0
        
        q, visited = [(beginWord, 1)], set()
        while q:
            word, step = q.pop(0)
            if word not in visited:
                visited.add(word)
                if word == endWord:
                    return step
                for i in range(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":  # 26 directions
                        temp = word[:i] + j + word[i+1:]
                        if temp in wordDict and temp not in visited:  # different ways from beginWord to endWord
                            q.append((temp, step + 1))
        return 0
```

##### 解法二

**双向BFS**

```
start: hit
end: cog
wordDict: hot dot dog lot log 
stack:

首先，start 先转换，然后判断转换后的 temp 是否在 wordDict 中，如果不在就继续替换，如果在就判断是否在 end 中，如果在就返回 step + 1，如果不在就将 temp 加入到 stack 中。

start: hit
end: cog
wordDict: hot dot dog lot log 
stack: hot

然后判断 len(stack) < len(end)，如果是就将 start 替换为 stack，如果不是就将 start 替换为 end 并且将 end 替换为 stack，同时将 step + 1。

start: cog
end: hot
wordDict: hot dot dog lot log 
stack: hot

现在就相当于找 cog->hot 的最短路径，也就是从后往前找了。重复上述步骤直到 start 和 end 都为空，此时应该返回 0 表示没有找到路径。
```

##### Python3代码

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # solution two: Double BFS
        wordDict, step = set(wordList), 1
        if endWord not in wordDict:
            return 0
        start, end = set([beginWord]), set([endWord])
        while start:
            stack = set([])
            wordDict -= start

            for s in start:
                for i in range(len(beginWord)):
                    for j in string.ascii_lowercase:  # a-z
                        temp = s[:i] + j + s[i+1:]
                        if temp not in wordDict:
                            continue
                        if temp in end:
                            return step + 1
                        stack.add(temp)
            if len(stack) < len(end):
                start = stack
            else:
                start, end = end, stack
            step += 1
        return 0
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0127-Word-Ladder/0127.py)

### 参考

[Leetcode 127：单词接龙（最详细的解法！！！）](https://coordinate.wang/index.php/archives/2225/)