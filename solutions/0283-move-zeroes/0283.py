class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # solution 1
        n = len(nums)
        left, right = 0, 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        
        # solution 2
        count0 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            elif count0 != 0:
                nums[i - count0], nums[i] = nums[i], 0
        
        # solution 3
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1