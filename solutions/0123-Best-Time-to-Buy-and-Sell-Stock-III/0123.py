from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_2_0, dp_i_1_0 = 0, 0
        # dp_i_2_1, dp_i_1_1 = -prices[0], -prices[0]  # 会报错：list index out of range
        dp_i_2_1, dp_i_1_1 = float('-inf'), float('-inf')  # 负无穷
        for i in range(len(prices)):
            # 昨天没有股票，昨天有股票今天卖出
            dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + prices[i])
            # 昨天有股票，昨天没有股票今天买入
            dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - prices[i])
            # 昨天没有股票，昨天有股票今天卖出
            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + prices[i])
            # 昨天有股票，昨天没有股票今天买入
            dp_i_1_1 = max(dp_i_1_1, -prices[i])
            
        return dp_i_2_0

if __name__ == "__main__":
    prices = [3,3,5,0,0,3,1,4]
    print(Solution().maxProfit(prices))