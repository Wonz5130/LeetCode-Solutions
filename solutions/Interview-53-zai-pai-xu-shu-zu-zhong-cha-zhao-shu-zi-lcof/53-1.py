class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # 求右边界
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        R = right
        
        # 如果R越界或者R位置的值不等于target，说明不存在target，可以直接返回0
        if R < 0 or nums[R] != target:
            return 0
        left = 0
        # 缩小区间，直接在[0,R]中寻找左边界
        right = R
        # 求左边界
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        L = left
        return R - L + 1