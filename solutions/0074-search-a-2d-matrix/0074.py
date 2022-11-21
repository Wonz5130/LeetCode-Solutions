class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        left0, right0 = 0, m
        while left0 < right0:
            mid0 = (left0 + right0 + 1) >> 1
            if matrix[mid0][0] == target:
                return True
            # 将区间划分成[left, mid - 1]和[mid, right]
            elif matrix[mid0][0] < target:
                left0 = mid0
            else:
                right0 = mid0 - 1
        left1, right1 = 0, n
        while left1 <= right1:
            mid1 = (left1 + right1) >> 1
            if matrix[left0][mid1] == target:
                return True
            elif matrix[left0][mid1] < target:
                left1 = mid1 + 1
            else:
                right1 = mid1 - 1
        return False