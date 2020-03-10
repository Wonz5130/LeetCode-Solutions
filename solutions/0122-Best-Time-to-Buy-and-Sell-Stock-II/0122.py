from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution one: 贪心
        if not prices or len(prices) == 0:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            if(prices[i+1] > prices[i]):
                profit += prices[i+1] - prices[i]
        return profit

        # solution two: 动态规划
        dp_i_0 = 0
        dp_i_1 = float('-inf')  # 负无穷
        for i in range(len(prices)):
            temp = dp_i_0
            # 昨天没有股票，昨天有股票今天卖出
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])  # dp_i_0 和 dp_i_1 可以看成是变量，存储的都是上一次即昨天的值
            # 昨天有股票，昨天没有股票今天买入
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))