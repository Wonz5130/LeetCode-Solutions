class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 先上下镜面翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
        
        # 再主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]