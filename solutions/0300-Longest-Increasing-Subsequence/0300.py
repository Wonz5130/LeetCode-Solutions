from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # # solution one: 动态规划
        # n = len(nums)
        # dp = [1] * n  # 初始化每个都为 1
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        
        # res = 0
        # for i in range(n):
        #     res = max(res, dp[i])
        # return res

        # solution two: 二分
        n = len(nums)
        top = [0] * n
        # 牌堆数初始化为 0
        piles = 0
        for i in nums:
            poker = i

            # 搜索左侧边界的二分查找
            left, right = 0, piles
            while left < right:
                mid = int((left + right) / 2)
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid
            
            # 新建一个牌堆
            if left == piles:
                piles += 1
            # 把这张牌放到牌堆顶
            top[left] = poker
        
        # 牌堆数就是 LTS 长度
        return piles

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums))