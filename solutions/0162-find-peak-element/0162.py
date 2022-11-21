class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]
        
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) >> 1
            if get(mid - 1) < get(mid) > get(mid + 1):
                return mid
            elif get(mid) < get(mid + 1):
                left = mid + 1
            elif get(mid) > get(mid + 1):
                right = mid - 1