class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution one: binary search
        low, high = 0, len(nums) - 1
        while low < high:
            mid = int((low + high) / 2)  # element in list must be int
            if mid % 2 == 1:  # even position
                mid -= 1
            if nums[mid] != nums[mid + 1]:  # result is on the left of mid
                high = mid
            else:
                low = mid + 2
        return nums[low]

        # # solution two: adjacent elements are equal
        # for i in range(0, len(nums) - 1, 2):  # step = 2
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        # return nums[-1]

if __name__ == "__main__":
    nums = [1,1,2,3,3,4,4,8,8]
    print(Solution().singleNonDuplicate(nums))