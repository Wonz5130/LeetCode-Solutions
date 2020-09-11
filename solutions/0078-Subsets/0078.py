from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(nums, start, path):
            # 加入 path
            res.append(path)
            # i 从 start 开始递增
            for i in range(start, n):
                # 回溯及更新 path
                # path.append([nums[i]])
                backtrack(nums, i + 1, path + [nums[i]])
                # path.pop()
        
        backtrack(nums, 0, [])
        return res

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().subsets(nums))