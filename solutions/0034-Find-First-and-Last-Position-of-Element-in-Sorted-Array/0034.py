class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # solution 
        if len(nums) == 0:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        if nums[right] != target:
            return [-1, -1]
        left_bound = right

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) >> 1
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1

        return [left_bound, right]
    #     # solution 1
    #     left = self.left_bound(nums, target)
    #     right = self.right_bound(nums, target)
    #     if left > right:
    #         return [-1, -1]
    #     return [left, right]
    
    # def left_bound(self, nums: List[int], target: int) -> int:
    #     # 左闭右闭
    #     left, right = 0, len(nums) - 1
    #     # 循环结束：left > right
    #     while left <= right:
    #         mid = (left + right) >> 1
    #         if nums[mid] < target:
    #             left = mid + 1
    #         elif nums[mid] > target:
    #             right = mid - 1
    #         # 锁定左边界
    #         else:
    #             right = mid - 1
    #     # 检查 left 越界
    #     if left >= len(nums) or nums[left] != target:
    #         return -1
    #     return left

    
    # def right_bound(self, nums: List[int], target: int) -> int:
    #     # 左闭右闭
    #     left, right = 0, len(nums) - 1
    #     # 循环结束：left > right
    #     while left <= right:
    #         mid = (left + right) >> 1
    #         if nums[mid] < target:
    #             left = mid + 1
    #         elif nums[mid] > target:
    #             right = mid - 1
    #         # 锁定右边界
    #         else:
    #             left = mid + 1
    #     # 检查 right 越界
    #     if right < 0 or nums[right] != target:
    #         return -1
    #     return right

    #     # solution one: binary search
    #     left = self.lowwer_bound(nums, target)
    #     right = self.higher_bound(nums, target)
    #     if left == right:
    #         return [-1, -1]
    #     return [left, right - 1]
    
    # def lowwer_bound(self, nums, target):
    #     # find in range [left, right)
    #     left, right = 0, len(nums)
    #     while left < right:
    #         mid = int((left + right) / 2)
    #         if nums[mid] < target:  # <
    #             left = mid + 1
    #         else:
    #             right = mid
    #     return left
    
    # def higher_bound(self, nums, target):
    #     # find in range [left, right)
    #     left, right = 0, len(nums)
    #     while left < right:
    #         mid = int((left + right) / 2)
    #         if nums[mid] <= target:  # <=
    #             left = mid + 1
    #         else:
    #             right = mid
    #     return left

        # # solution two: bisect
        # left = bisect.bisect_left(nums, target)
        # right = bisect.bisect_right(nums, target)
        # if left == right:
        #     return [-1, -1]
        # return [left, right - 1]
        
if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    print(Solution().searchRange(nums, target))