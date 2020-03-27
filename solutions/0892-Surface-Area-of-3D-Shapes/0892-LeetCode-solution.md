> LeetCode 0892. Surface Area of 3D Shapes三维形体的表面积【Easy】【Python】【数学】

### Problem

[LeetCode](https://leetcode.com/problems/surface-area-of-3d-shapes/)

On a `N * N` grid, we place some `1 * 1 * 1 `cubes.

Each value `v = grid[i][j]` represents a tower of `v` cubes placed on top of grid cell `(i, j)`.

Return the total surface area of the resulting shapes.

**Example 1:**

```
Input: [[2]]
Output: 10
```

**Example 2:**

```
Input: [[1,2],[3,4]]
Output: 34
```

**Example 3:**

```
Input: [[1,0],[0,2]]
Output: 16
```

**Example 4:**

```
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
```

**Example 5:**

```
Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
```

**Note:**

- `1 <= N <= 50`
- `0 <= grid[i][j] <= 50`

### 问题

[力扣](https://leetcode-cn.com/problems/surface-area-of-3d-shapes/)

在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

请你返回最终形体的表面积。

**示例 1：**

```
输入：[[2]]
输出：10
```

**示例 2：**

```
输入：[[1,2],[3,4]]
输出：34
```

**示例 3：**

```
输入：[[1,0],[0,2]]
输出：16
```

**示例 4：**

```
输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：32
```

**示例 5：**

```
输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：46
```

**提示：**

* `1 <= N <= 50`
* `0 <= grid[i][j] <= 50`

### 思路

**数学**

```
从反面来考虑，先计算有多少叠起来的面，最后减去叠起来面。

叠起来的 v 个立方体有 v-1 个接触面，分两种情况：
1. 当前柱子与上边柱子接触
2. 当前柱子与左边柱子接触
```

**时间复杂度:** O(n^2)
**空间复杂度:** O(1)

##### Python3代码

```python
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cubes, faces = 0, 0
        for i in range(n):
            for j in range(n):
                cubes += grid[i][j]
                if grid[i][j] > 0:
                    # 叠起来的 v 个立方体有 v-1 个接触面
                    faces += grid[i][j] - 1
                if i > 0:
                    # 当前柱子与上边柱子的接触面数量
                    faces += min(grid[i-1][j], grid[i][j])
                if j > 0:
                    # 当前柱子与左边柱子的接触面数量
                    faces += min(grid[i][j-1], grid[i][j])
        return 6 * cubes - 2 * faces
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0892-Surface-Area-of-3D-Shapes/0892.py)