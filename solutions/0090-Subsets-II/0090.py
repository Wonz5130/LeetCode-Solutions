from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        # 先对 nums 进行排序
        nums.sort()

        def backtrack(nums, start, path):
            # 加入 res
            res.append(path)
            # i 从 start 开始递增
            for i in range(start, n):
                # 剪枝：当前元素和前一个元素相同
                if i > start and nums[i - 1] == nums[i]:
                    continue
                # 回溯及更新 path
                # path.append([nums[i]])
                backtrack(nums, i + 1, path + [nums[i]])
                # path.pop()
        
        backtrack(nums, 0, [])
        return res

if __name__ == "__main__":
    nums = [1,2,2]
    print(Solution().subsetsWithDup(nums))