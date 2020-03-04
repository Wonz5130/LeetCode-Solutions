from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fresh = 0
        q = []

        # count fresh oranges and enqueue rotten oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        if fresh == 0:
            return 0
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        minute = 0
        
        # bfs
        while q:
            if fresh == 0:
                return minute
                
            size = len(q)
            for i in range(size):
                x, y = q.pop(0)
                for d in dirs:
                    nx, ny = x + d[0], y + d[1]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    q.append((nx, ny))
                    fresh -= 1
            minute += 1

        if fresh != 0:
            return -1

if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(Solution().orangesRotting(grid))