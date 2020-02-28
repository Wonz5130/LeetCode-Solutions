from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ans = 0
        self.island = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:  # 1: island
                    self.dfs(grid, i, j)
                    self.ans = max(self.ans, self.island)
                    self.island = 0
        return self.ans
    
    # dfs template
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        grid[i][j] = 0
        self.island += 1
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for direction in directions:
            x, y = i + direction[0], j + direction[1]
            if 0 <= x < m and 0 <= y < n and grid[x][y]:
                self.dfs(grid, x, y)

if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(Solution().maxAreaOfIsland(grid))