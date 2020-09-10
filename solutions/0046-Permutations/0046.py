from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # solution one: permutations
        return list(permutations(nums))

        # solution two: recursion
        res = []
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])
        
        # solution three: backtracking
        visited = [0] * len(nums)
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0
        
        dfs([])
        return res

        # solution four: backtracking
        res = []
        n = len(nums)
        visited = [0] * n
        def backtrack(nums, path):
            # 1. 递归终止情况
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                # 3. 剪枝
                # 下面这种方法不够高效
                # if nums[i] in path:
                #     continue
                # 使用 visited 来标记是否已经被访问过
                if not visited[i]:
                    visited[i] = 1
                    # 2. 回溯以及更新 path
                    path.append(nums[i])
                    backtrack(nums, path)
                    path.pop()
                    visited[i] = 0
        
        backtrack(nums, [])
        return res

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute(nums))        