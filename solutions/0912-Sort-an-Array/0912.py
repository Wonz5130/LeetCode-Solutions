from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # solution one: 自带sort
        # return sorted(nums)

        # # solution two: 快排
        # # 20221116：通过不了
        # n = len(nums)

        # def quick(left, right):
        #     if left >= right:
        #         return nums
            
        #     pivot = left
        #     i, j = left, right
            
        #     while i < j:
        #         # 先右
        #         while i < j and nums[j] > nums[pivot]:
        #             j -= 1
        #         # 再左
        #         while i < j and nums[i] <= nums[pivot]:
        #             i += 1
        #         nums[i], nums[j] = nums[j], nums[i]
        #     nums[pivot], nums[j] = nums[j], nums[pivot]
        #     quick(left, j - 1)
        #     quick(j + 1, right)
        #     return nums
        
        # return quick(0, n - 1)

    #     # solution three
    #     self.quick_sort(nums, 0, len(nums) - 1)
    #     return nums

    # def quick_sort(self, nums: List[int], left: int, right: int):
    #     if left >= right:
    #         return
    #     pivot = self.partition(nums, left, right)
    #     self.quick_sort(nums, left, pivot - 1)
    #     self.quick_sort(nums, pivot + 1, right)
    
    # def partition(self, nums: List[int], left: int, right: int) -> int:
    #     pivot = left
    #     i, j = left, right
    #     while i < j:
    #         while i < j and nums[j] > nums[pivot]:
    #             j -= 1
    #         while i < j and nums[i] <= nums[pivot]:
    #             i += 1
    #         nums[i], nums[j] = nums[j], nums[i]
    #     nums[pivot], nums[j] = nums[j], nums[pivot]
    #     return i

        # # solution four: 对称双路快排
        # # 20221116：通过
        # def quicksort(left, right):
        #     if left >= right:
        #         return
        #     pivot = nums[random.randint(left, right)]
        #     i, j = left, right
        #     while i <= j:
        #         if nums[i] >= pivot > nums[j] or nums[i] > pivot >= nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #         if nums[i] <= pivot:
        #             i += 1
        #         if nums[j] >= pivot:
        #             j -= 1
                
        #     quicksort(left, j)
        #     quicksort(i, right)

        # quicksort(0, len(nums) - 1)
        # return nums

        # solution 5: 合并排序
        def merge_sort(left, right):
            if left == right:
                return
            mid = (left + right) >> 1
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            tmp = []
            i, j = left, mid + 1
            while i <= mid or j <= right:
                # i 已移到末尾 or nums[j] < nums[i]
                if i > mid or (j <= right and nums[j] < nums[i]):
                    tmp.append(nums[j])
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            nums[left: right + 1] = tmp
        
        merge_sort(0, len(nums) - 1)
        return nums