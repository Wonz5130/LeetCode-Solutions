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