class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp, prev = 0, 0
        sum = -0xFFFFFFFF
        for i in range(len(nums)):
            dp = nums[i] + (prev if prev > 0 else 0)  # if prev > 0: dp = nums[i] + prev, else: dp = num[i]
            prev = dp  # update prev every time
            sum = max(sum, dp)
        return sum
        
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))