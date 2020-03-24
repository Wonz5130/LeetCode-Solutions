class Solution:
    def massage(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        res = 0
        # dp[0] = dp[1] = 0, dp[i] 对应 nums[i - 2]
        for i in range(2, len(nums) + 2):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
            res = max(res, dp[i])
        return res