from typing import List

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        self.res = 0

        graph = [[[None] for x in range(n)] for x in range(n)]
        for i in range(len(relation)):
            graph[relation[i][0]][relation[i][1]] = 1

        def dfs(start, step):
            if step > k:
                return
            # 经过 k 轮传到 n-1
            if step == k and start == n - 1:
                self.res += 1
                return
            for i in range(n):
                # 有下一个可传
                if graph[start][i] == 1:
                    dfs(i, step + 1)

        dfs(0, 0)
        return self.res

if __name__ == "__main__":
    n = 5
    relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]
    k = 3
    print(Solution().numWays(n, relation, k))