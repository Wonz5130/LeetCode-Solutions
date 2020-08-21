class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # 初始位置是雷，直接改为 X 退出
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        self.m, self.n = len(board), len(board[0])
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))

        # 检查周围雷的情况
        def check(i, j):
            cnt = 0
            for x, y in direction:
                x, y = x + i, y + j
                if 0 <= x < self.m and 0 <= y < self.n and board[x][y] == 'M':
                    cnt += 1
            return cnt
        
        # DFS
        def dfs(i ,j):
            cnt = check(i, j)
            # 周围没有雷
            if not cnt:
                board[i][j] = 'B'
                for x, y in direction:
                    x, y = x + i, y + j
                    if 0 <= x < self.m and 0 <= y < self.n and board[x][y] == 'E':
                        dfs(x, y)
            # 标记周围有雷
            else:
                board[i][j] = str(cnt)
        dfs(click[0], click[1])
        return board