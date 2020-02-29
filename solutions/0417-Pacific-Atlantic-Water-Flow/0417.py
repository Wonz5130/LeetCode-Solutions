from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False] * n for x in range(m)]  # Pacific
        a_visited = [[False] * n for x in range(m)]  # Atlantic

        # left and right
        for i in range(m):
            self.dfs(p_visited, matrix, m, n, i, 0)
            self.dfs(a_visited, matrix, m, n, i, n - 1)
        
        # up and down
        for j in range(n):
            self.dfs(p_visited, matrix, m, n, 0, j)
            self.dfs(a_visited, matrix, m, n, m - 1, j)
        
        ans = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    ans.append([i, j])
        return ans

    def dfs(self, visited, matrix, m, n, i, j):
        visited[i][j] = True
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for d in directions:
            x, y = i + d[0], j + d[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:  # [x, y] < [i, j]
                continue
            self.dfs(visited, matrix, m, n, x, y)

if __name__ == "__main__":
    matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(Solution().pacificAtlantic(matrix))