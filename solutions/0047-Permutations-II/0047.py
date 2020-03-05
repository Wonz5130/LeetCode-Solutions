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

if __name__ == "__main__":
    nums = [1,1,2]
    print(Solution().permuteUnique(nums))    