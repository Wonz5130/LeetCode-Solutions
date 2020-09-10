from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
            # 防止出现这种情况：一个数字使用多次
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # 2.backtrack and update 回溯以及更新 path
            path.append(candidates[i])
            self.dfs(candidates, i + 1, n, path, res, tmp)
            path.pop()

if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    # candidates = [2,5,2,1,2]
    # target = 5
    print(Solution().combinationSum2(candidates, target))  