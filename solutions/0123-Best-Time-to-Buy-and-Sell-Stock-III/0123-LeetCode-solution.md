> LeetCode 0123. Best Time to Buy and Sell Stock III买卖股票的最佳时机 III【Hard】【Python】【动态规划】

### Problem

[LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete at most *two* transactions.

**Note:** You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

**Example 1:**

```
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```

**Example 2:**

```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

**Example 3:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

### 问题

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

**注意:** 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例 1:**

```
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
```

**示例 2:**

```
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
```

**示例 3:**

```
输入: [7,6,4,3,1] 
输出: 0 
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
```

### 思路

**动态规划**

```
找到状态方程

dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
解释：昨天没有股票，昨天有股票今天卖出

dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
解释：昨天有股票，昨天没有股票今天买入

base case：
dp[-1][k][0] = dp[i][k][0] = 0
dp[-1][k][1] = dp[i][k][1] = -inf

k = 2
因为 k 为 2，所以要对 k 进行穷举。
dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
dp[i][1][1] = max(dp[i-1][1][1], -prices[i])

i = 0 时，dp[i-1] 不合法。
dp[0][1][0] = max(dp[-1][1][0], dp[-1][1][1] + prices[i])
            = max(0, -infinity + prices[i])
            = 0
dp[0][1][1] = max(dp[-1][1][1], dp[-1][1][0] - prices[i])
            = max(-infinity, 0 - prices[i]) 
            = -prices[i]
dp[0][2][0] = max(dp[-1][2][0], dp[-1][2][1] + prices[i])
            = max(0, -infinity + prices[i])
            = 0
dp[0][2][1] = max(dp[-1][2][1], dp[-1][2][0] - prices[i])
            = max(-infinity, 0 - prices[i])
            = -prices[i]
```

**空间复杂度:** O(1)

##### Python3代码

```python
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
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0123-Best-Time-to-Buy-and-Sell-Stock-III/0123.py)

### 参考

[一个方法团灭 6 道股票问题](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/)