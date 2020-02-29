from typing import List

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        m = len(M)
        ans, visited = 0, set()

        # def template
        def dfs(i):
            for j in range(m):
                if M[i][j] and j not in visited:  # 1 and not visited
                    visited.add(j)
                    dfs(j)

        for i in range(m):
            if i not in visited:  # not visited
                dfs(i)
                ans += 1
        return ans

if __name__ == "__main__":
    M = [[1,1,0],
         [1,1,0],
         [0,0,1]]
    print(Solution().findCircleNum(M))