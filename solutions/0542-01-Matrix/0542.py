import collections

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # bfs: 不记录层数
        m, n = len(matrix), len(matrix[0])
        q = collections.deque()
        res = [[None] * n for _ in range(m)]

        # 把所有 0 放入队列
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    res[i][j] = 0
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                newx, newy = x + dx, y + dy
                if 0 <= newx < m and 0 <= newy < n and res[newx][newy] == None:  # 当前为 1
                    res[newx][newy] = res[x][y] + 1
                    q.append((newx, newy))
        return res