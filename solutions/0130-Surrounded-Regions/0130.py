from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":  # change "O" to "*"
                board[i][j] = "*"
                for k in range(4):
                    dfs(i + directions[k][0], j + directions[k][1])
        
        # search left and right
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        
        # search up and down
        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":  # change "O" to "X"
                    board[i][j] = "X"
                elif board[i][j] == "*":  # change "*" to "O"
                    board[i][j] = "O"

if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Solution().solve(board)
    print(board)