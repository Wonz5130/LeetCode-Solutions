from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # solution one: recursion
        res = []
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, path):
        if not nums and path not in res:  # path should be unique
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])
        
        # solution two: backtracking
        nums.sort()  # sort at first
        self.res = []
        check = [0 for _ in range(len(nums))]

        self.dfs([], nums, check)
        return self.res
    
    def dfs(self, sol, nums, check):
        # 1.valid result
        if len(sol) == len(nums):
            self.res.append(sol)
            return
        
        for i in range(len(nums)):
            # 3.pruning
            if check[i] == 1:  # used
                continue
            if i > 0 and nums[i] == nums[i - 1] and not check[i - 1]:
                continue

            # 2.backtrack and update check
            check[i] = 1
            self.dfs(sol + [nums[i]], nums, check)
            check[i] = 0  # after backtracking, should update check[i]
        
        # solution three: backtracking
        res = []
        n = len(nums)
        visited = [0] * n
        # 先排序
        nums.sort()

        def backtrack(nums, path):
            # 1. 递归终止情况
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                # 3. 剪枝
                # 剪掉这种情况：已经访问过
                if visited[i] == 1:
                    continue
                # 剪掉这种情况：前一个数字没有被访问过且当前数字和前一个数字相同
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                # 2. 回溯以及更新 path
                visited[i] = 1
                path.append(nums[i])
                backtrack(nums, path)
                path.pop()
                visited[i] = 0
        
        backtrack(nums, [])
        return res

if __name__ == "__main__":
    nums = [1,1,2]
    print(Solution().permuteUnique(nums))    