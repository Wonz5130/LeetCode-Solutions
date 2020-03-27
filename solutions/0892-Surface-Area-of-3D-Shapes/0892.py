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