class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # 左闭右闭
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                # 左半边有序
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                elif nums[mid] == target:
                    return mid
                else:
                    left = mid + 1
            else:
                # 右半边有序
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                elif nums[mid] == target:
                    return mid
                else:
                    right = mid - 1
        return -1