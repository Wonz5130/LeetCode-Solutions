> LeetCode 0079. Word Search单词搜索【Medium】【Python】【DFS】

### Problem

[LeetCode](https://leetcode.com/problems/word-search/)

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example:**

```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```

### 问题

[力扣](https://leetcode-cn.com/problems/word-search/)

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

**示例:**

```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
```

### 思路

**DFS**

```
DFS 四个方向搜索，访问过的标记为 '#' 表示不可重复访问。
记得访问结束要恢复，因为还有其他路径。
```

##### Python3代码

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp, board[i][j] = board[i][j], '#'  # '#': visited
        ans = self.dfs(board, i - 1, j, word[1:]) or self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i, j - 1, word[1:]) or self.dfs(board, i, j + 1, word[1:])
        board[i][j] = tmp  # recover board[i][j]
        return ans
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0079-Word-Search/0079.py)