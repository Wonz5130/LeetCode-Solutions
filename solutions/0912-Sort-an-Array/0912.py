from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # solution one: 自带sort
        return sorted(nums)

        # solution two: 快排
        n = len(nums)

        def quick(left, right):
            if left >= right:
                return nums
            
            pivot = left
            i, j = left, right
            
            while i < j:
                # 先右
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                # 再左
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[j] = nums[j], nums[pivot]
            quick(left, j - 1)
            quick(j + 1, right)
            return nums
        
        return quick(0, n - 1)