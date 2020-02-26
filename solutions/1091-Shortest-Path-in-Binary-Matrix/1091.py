from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:  # top-left is not empty or bottom-right is not empty
            return -1

        # eight directions: → ← ↓ ↑ ↗ ↙ ↖ ↘
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        
        queue = [(0, 0, 1)]  # location, cnt
        n = len(grid)

        # BFS
        while len(queue):
            x0, y0, cnt = queue.pop(0)  # pop (location, cnt)
            if x0 == n - 1 and y0 == n - 1:  # already arrive at bottom-right
                return cnt

            # eight directions
            for i, j in directions:
                x, y = x0 + i, y0 + j
                # (x, y) is in the grid and grid[x][y] = 0, also means: grid[x][y] is not visited
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    queue.append((x, y, cnt + 1))
                    grid[x][y] = 1  # visited
        
        return -1

if __name__ == "__main__":
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    print(Solution().shortestPathBinaryMatrix(grid))