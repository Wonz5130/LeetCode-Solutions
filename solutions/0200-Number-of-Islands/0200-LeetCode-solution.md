> LeetCode 0200. Number of Islands岛屿数量【Medium】【Python】【DFS】

### Problem

[LeetCode](https://leetcode.com/problems/number-of-islands/)

Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

```
Input:
11110
11010
11000
00000

Output: 1
```

**Example 2:**

```
Input:
11000
11000
00100
00011

Output: 3
```

### 问题

[力扣](https://leetcode-cn.com/problems/number-of-islands/)

给定一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

**示例 1:**

```
输入:
11110
11010
11000
00000

输出: 1
```

**示例 2:**

```
输入:
11000
11000
00100
00011

输出: 3
```

### 思路

**DFS**

```
对每个 "1" 进行 DFS，把它四周相邻的所有 “1” 全变为 “0”。
计算总的 DFS 次数，就是岛的个数。
```

**时间复杂度:** O(m\*n)，m 为行数，n 为列数。
**空间复杂度:** 最坏情况下为 O(m\*n)，此时全部都是陆地。

##### Python3代码

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        # m, n = len(grid), len(grid[0])  # Runtime Error
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    ans += 1
        return ans
    
    # dfs template
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        grid[i][j] = "0"
        for direction in directions:
            x, y = i + direction[0], j + direction[1]
            if 0 <= x < m and 0 <= y < n:
                if grid[x][y] == "1":  # change "1" to "0"
                    self.dfs(grid, x, y)
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0200-Number-of-Islands/0200.py)