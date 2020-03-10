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
            # 昨天没有股票，昨天有股票今天卖出
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])  # dp_i_0 和 dp_i_1 可以看成是变量，存储的都是上一次即昨天的值
            # 昨天有股票，昨天没有股票今天买入
            dp_i_1 = max(dp_i_1, -prices[i])  
        return dp_i_0
  
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))