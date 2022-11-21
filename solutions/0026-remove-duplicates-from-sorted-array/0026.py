class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast, slow = 1, 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast] 
                slow += 1
            fast += 1

        return slow

        # index = 0
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[index]:
        #         index += 1
        #         nums[index] = nums[i]
        # return index + 1