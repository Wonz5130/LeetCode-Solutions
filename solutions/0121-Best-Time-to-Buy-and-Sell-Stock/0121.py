from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution one: 贪心
        profit, buy = 0, 0x7FFFFFFF
        for price in prices:
            if buy > price:
                buy = price  # 尽量买入价格小的股票
            if profit < price - buy:
                profit = price - buy  # 尽量在最大价格卖出股票
        return profit

        # solution two: 动态规划
        # K = 1
        dp_i_0 = 0
        dp_i_1 = float('-inf')  # 负无穷
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])  # 前面没有股票，前面有股票现在卖出
            dp_i_1 = max(dp_i_1, -prices[i])  # 前面有股票，前面没有股票现在买入
        return dp_i_0
  
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))