class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # 一维列表
        board = ['.' * n for _ in range(n)]

        def isValid(board, row, col):
            """
            检查是否有皇后互相冲突
            """
            # 检查第 row 行 第 col 列是否可以放皇后
            # 只需考虑 <= row，因为后面的棋盘是空的
            for row_index in range(row):
                # 判断当前行是否放了皇后
                if row_index == row:
                    if 'Q' in board[row_index]:
                        return False
                # 判断遍历每行时，第 col 列是否已经放了皇后
                if 'Q' == board[row_index][col]:
                    return False
            
            # 判断左上方是否放了皇后
            tmp_row, tmp_col = row, col
            while tmp_row > 0 and tmp_col > 0:
                tmp_row -= 1
                tmp_col -= 1
                if 'Q' in board[tmp_row][tmp_col]:
                    return False

            # 判断右上方是否放了皇后
            tmp_row, tmp_col = row, col
            while tmp_row > 0 and tmp_col < n - 1:
                tmp_row -= 1
                tmp_col += 1
                if 'Q' in board[tmp_row][tmp_col]:
                    return False
            
            return True
        
        def replace_char(string, char, index):
            """
            构建新的字符串进行赋值
            """
            string = list(string)
            string[index] = char
            return ''.join(string)

        def backtrack(board, row):
            # 1.结束条件
            if row == len(board):
                # 需要用 list 转化一下
                res.append(list(board[:]))
                return
            
            # 2.剪枝
            # m = len(board[row])
            for col in range(n):
                # 剪枝
                if not isValid(board, row, col):
                    continue
                # 3.回溯并更新 row
                board[row] = replace_char(board[row], 'Q', col)
                # board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row] = replace_char(board[row], '.', col)
                # board[row][col] = '.'
        
        backtrack(board, 0)
        return res

if __name__ == "__main__":
    n = 4
    print(Solution().solveNQueens(n))