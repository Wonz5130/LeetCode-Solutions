> LeetCode 0130. Surrounded Regions被围绕的区域【Medium】【Python】【DFS】

### Problem

[LeetCode](https://leetcode.com/problems/surrounded-regions/)

Given a 2D board containing `'X'` and `'O'` (**the letter O**), capture all regions surrounded by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

**Example:**

```
X X X X
X O O X
X X O X
X O X X
```

After running your function, the board should be:

```
X X X X
X X X X
X X X X
X O X X
```

**Explanation:**

Surrounded regions shouldn’t be on the border, which means that any `'O'` on the border of the board are not flipped to `'X'`. Any `'O'` that is not on the border and it is not connected to an `'O'` on the border will be flipped to `'X'`. Two cells are connected if they are adjacent cells connected horizontally or vertically.

### 问题

[力扣](https://leetcode-cn.com/problems/surrounded-regions/)

给定一个二维的矩阵，包含 `'X'` 和 `'O'`（**字母 O**）。

找到所有被 `'X'` 围绕的区域，并将这些区域里所有的 `'O'` 用 `'X'` 填充。

**示例:**

```
X X X X
X O O X
X X O X
X O X X
```

运行你的函数后，矩阵变为：

```
X X X X
X X X X
X X X X
X O X X
```


**解释:**

被围绕的区间不会存在于边界上，换句话说，任何边界上的 `'O'` 都不会被填充为 `'X'`。 任何不在边界上，或不与边界上的 `'O'` 相连的 `'O'` 最终都会被填充为 `'X'`。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

### 思路

**DFS**

```
从反面来想。
先找到边界（即上下左右四条边）上的 "O"，先变为 "*"。
再遍历 board 矩阵，将 "O" 变为 "X"，再将 "*" 变为 "O"。
这样问题就变成从边界找连通的 "O"，就可以用 DFS 了。
```

**时间复杂度:** O(m\*n)，m 是行数，n 是列数。
**空间复杂度:** O(1)，因为是在 board 矩阵基础上进行改动。

##### Python3代码

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":  # change "O" to "*"
                board[i][j] = "*"
                for k in range(4):
                    dfs(i + directions[k][0], j + directions[k][1])
        
        # search left and right
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        
        # search up and down
        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":  # change "O" to "X"
                    board[i][j] = "X"
                elif board[i][j] == "*":  # change "*" to "O"
                    board[i][j] = "O"
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0130-Surrounded-Regions/0130.py)