from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp_i_0 = 0
        dp_i_1 = float('-inf')  # 负无穷
        for i in range(len(prices)):
            temp = dp_i_0
            # 昨天没有股票，昨天有股票今天卖出，同时减去交易费用
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)  # dp_i_0 和 dp_i_1 可以看成是变量，存储的都是上一次即昨天的值
            # 昨天有股票，昨天没有股票今天买入
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0

if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(Solution().maxProfit(prices, fee))