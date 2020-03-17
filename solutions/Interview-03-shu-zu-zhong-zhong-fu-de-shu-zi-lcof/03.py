from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # solution one: 哈希表
        n = len(nums)
        flag = [False for i in range(n)]
        for i in range(n):
            if flag[nums[i]] == False:
                flag[nums[i]] = True
            else:
                return nums[i]
        return -1

        # solution two: 排序
        nums.sort()
        pre = nums[0]
        for i in range(1, len(nums)):
            if pre == nums[i]:
                return nums[i]
            else:
                pre = nums[i]
        return -1

        # solution three
        n = len(nums)
        for i in range(n):
            if nums[i] == i:
                continue
            # 有重复
            elif nums[nums[i]] == nums[i]:
                return nums[i]
            # 交换
            else:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

if __name__ == "__main__":
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(Solution().findRepeatNumber(nums))