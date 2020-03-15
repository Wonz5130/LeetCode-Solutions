from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # solution one
        m, n = len(matrix), len(matrix[0])
        flag = 0
        res = []
        for i in range(m):
            min_ = max_ = matrix[i][0]
            for j in range(n):
                if matrix[i][j] < min_:
                    flag = j
                    min_ = matrix[i][j]
            max_ = min_
            for x in range(m):
                if matrix[x][flag] > max_:
                    break
                elif x == m - 1:
                    res.append(max_)
        return res

        # solution two
        min_ = {min(rows) for rows in matrix}
        max_ = {max(columns) for columns in zip(*matrix)}  # zip(*) 对矩阵进行转置，即找出每一列中的最大值
        return list(min_ & max_)

if __name__ == "__main__":
    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    print(Solution().luckyNumbers (matrix))