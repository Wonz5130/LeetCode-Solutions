> LeetCode 0188. Best Time to Buy and Sell Stock IV买卖股票的最佳时机 IV【Hard】【Python】【动态规划】

### Problem

[LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

Say you have an array for which the *i-*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete at most **k** transactions.

**Note:**
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

**Example 1:**

```
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
```

**Example 2:**

```
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
```

### 问题

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

**注意:** 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例 1:**

```
输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
```

**示例 2:**

```
输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
```

### 思路

**动态规划**

```
找到状态方程

dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
解释：昨天没有股票，昨天有股票今天卖出

dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
解释：昨天有股票，昨天没有股票今天买入

base case：
dp[-1][k][0] = dp[i][k][0] = 0
dp[-1][k][1] = dp[i][k][1] = -inf

k 如果超过 n/2，就当作是 inf 来处理。
k 如果没有超过 n/2，就列举出 k 的值。
```

**空间复杂度:** O(1)

##### Python3代码

```python
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
        # dp = [[[0] * 2] * (k+1)] * n  # 创建三维数组，这个有问题
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
```

### 代码地址

[GitHub链接]()