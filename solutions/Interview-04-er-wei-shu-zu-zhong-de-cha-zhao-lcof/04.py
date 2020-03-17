class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # solution one: 暴力
        # 特判
        if matrix == []:
            return False
        
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    break
        return False

        # solution two: 左下角标志数法
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
