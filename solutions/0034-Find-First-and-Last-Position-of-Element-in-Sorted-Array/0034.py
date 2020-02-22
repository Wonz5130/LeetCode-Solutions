class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # solution one: binary search
        left = self.lowwer_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]
    
    def lowwer_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] < target:  # <
                left = mid + 1
            else:
                right = mid
        return left
    
    def higher_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] <= target:  # <=
                left = mid + 1
            else:
                right = mid
        return left

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