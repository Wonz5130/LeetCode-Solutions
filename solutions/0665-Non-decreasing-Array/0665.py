class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # # solution one
        # if len(nums) <= 2:
        #     return True
        # nums1, nums2= nums[:], nums[:]
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         nums1[i] = nums[i+1]  # change bigger
        #         nums2[i+1] = nums[i]  # change smaller
        #         break  # only change once, then break
        # return nums1 == sorted(nums1) or nums2 == sorted(nums2)

        # solution two
        if len(nums) <= 2:
            return True
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                cnt += 1
                if i == 1 or nums[i-2] <= nums[i]:  # 3,5,4 -> 3,4,4
                    nums[i-1] = nums[i]
                else:  # 4,5,4 -> 4,5,5
                    nums[i] = nums[i-1]
                if cnt > 1:
                    return False
        return True

if __name__ == "__main__":
    nums = [4,2,1]
    print(Solution().checkPossibility(nums))