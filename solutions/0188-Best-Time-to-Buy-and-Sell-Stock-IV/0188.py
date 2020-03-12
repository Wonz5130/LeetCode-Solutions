from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k > n/2:
            # k = inf
            dp_i_0 = 0
            dp_i_1 = float('-inf')  # 负无穷
            for i in range(n):
                temp = dp_i_0
                # 昨天没有股票，昨天有股票今天卖出
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])  # dp_i_0 和 dp_i_1 可以看成是变量，存储的都是上一次即昨天的值
                # 昨天有股票，昨天没有股票今天买入
                dp_i_1 = max(dp_i_1, temp - prices[i])
            return dp_i_0
        
        # k <= len(prices)/2
        # dp = [[[0] * 2] * (k+1)] * n  # 创建三维数组，这么初始化三维列表，是浅复制，所以修改其中一个值会同时影响其他的值，所以这种方法不正确
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            for j in range(k, 0, -1):  # 逆序
                if i == 0:
                    dp[0][j][0] = 0
                    dp[0][j][1] = -prices[0]
                    continue
                # 昨天没有股票，昨天有股票今天卖出
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                # 昨天有股票，昨天没有股票今天买入，这里把买入当作一次交易，所以是 j-1
                # 如果把 j-1 写在上一行代码即把卖出当作一次交易，运行结果不是正确答案，不知道是为什么
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        
        return dp[n-1][k][0]

if __name__ == "__main__":
    prices = [3,3,5,0,0,3,1,4]
    k = 2
    print(Solution().maxProfit(k, prices))