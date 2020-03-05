from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # special judgment
        if n <= 0 or k <= 0 or k > n:
            return []
        
        res = []
        self.dfs(1, k, n, [], res)
        return res
    
    def dfs(self, start, k, n, path, res):
        # 1.valid result
        if len(path) == k:
            res.append(path[:])
            return
        
        # 3.pruning
        for i in range(start, n - (k - len(path)) + 2):
            # 2.backtrack and update
            path.append(i)
            self.dfs(i + 1, k, n, path, res)
            path.pop()

if __name__ == "__main__":
    n = 4
    k = 2
    print(Solution().combine(n, k))    