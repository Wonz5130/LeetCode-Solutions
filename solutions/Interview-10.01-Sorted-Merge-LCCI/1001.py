from typing import List

class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        # # solution one: sort
        # A[m:] = B
        # A.sort()

        # solution two: two point
        # B = []
        if n == 0:
            return
        i, j, k = m - 1, n - 1, m + n - 1
        while i > -1 and j > -1:  # > -1, if m = 0 or n = 0, then i = -1 or j = -1
            if A[i] <= B[j]:
                A[k] = B[j]
                k -= 1
                j -= 1
            else:
                A[k] = A[i]
                k -= 1
                i -= 1
        if j > -1:
            A[:j + 1] = B[:j  + 1]  # A = [], B = [1]

if __name__ == "__main__":
    A = [1,2,3,0,0,0]
    B = [2,5,6]
    m, n = 3, 3
    Solution().merge(A, m, B, n)
    print(A)