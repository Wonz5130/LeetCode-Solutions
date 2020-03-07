from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        if n == 0:
            return []
        
        # accelerate 剪枝提速，非必需
        candidates.sort()

        path, res = [], []
        self.dfs(candidates, 0, n, path, res, target)
        return res
    
    def dfs(self, candidates, start, n, path, res, target):
        # 1.valid result 递归终止情况
        if target == 0:
            res.append(path[:])
            return
        
        for i in range(start, n):
            tmp = target - candidates[i]
            # 3.pruning 剪枝
            if tmp < 0:
                break
            # 2.backtrack and update 回溯以及更新 path
            path.append(candidates[i])
            self.dfs(candidates, i, n, path, res, tmp)
            path.pop()

if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))  