class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = 0
        sum = -0xFFFFFFFF
        for i in range(len(nums)):
            dp = nums[i] + (dp if dp > 0 else 0)  # if dp > 0: dp = nums[i] + dp, else: dp = nums[i]
            sum = max(sum, dp)
        return sum
        
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))