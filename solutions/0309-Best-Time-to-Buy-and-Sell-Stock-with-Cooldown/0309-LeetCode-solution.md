> LeetCode 0309. Best Time to Buy and Sell Stock with Cooldown最佳买卖股票时机含冷冻期【Medium】【Python】【动态规划】

### Problem

[LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

**Example:**

```
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

### 问题

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

* 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
* 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

**示例:**

```
输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
```

### 思路

**动态规划**

```
找到状态方程

dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
解释：昨天没有股票，昨天有股票今天卖出

dp[i][k][1] = max(dp[i-1][k][1], dp[i- 2][k][0] - prices[i])
解释：昨天有股票，前天刚卖出股票昨天冷冻期今天买入
第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。

base case：
dp[-1][k][0] = dp[i][k][0] = 0
dp[-1][k][1] = dp[i][k][1] = -inf

k = +inf
因为 k 为正无穷，那么可以把 k 和 k-1 看成是一样的。
buy+sell = 一次完整的交易，这里把 sell 看成一次交易，所以第一行是 k-1。
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k-1][1] + prices[i])
			= max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-2][k][0] - prices[i])

所以 k 对状态转移没有影响：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

i = 0 时，dp[i-1] 不合法。
dp[0][0] = max(dp[-1][0], dp[-1][1] + prices[i])
         = max(0, -infinity + prices[i])
         = 0
dp[0][1] = max(dp[-1][1], dp[-1][0] - prices[i])
         = max(-infinity, 0 - prices[i]) 
         = -prices[i]
```

**空间复杂度:** O(1)

##### Python3代码

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0
        dp_i_1 = float('-inf')  # 负无穷
        dp_pre_0 = 0  # 表示 dp[i-2][0]
        for i in range(len(prices)):
            temp = dp_i_0
            # 昨天没有股票，昨天有股票今天卖出
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])  # dp_i_0 和 dp_i_1 可以看成是变量，存储的都是上一次即昨天的值
            # 昨天有股票，前天刚卖出股票昨天冷冻期今天买入
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp

        return dp_i_0
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0309-Best-Time-to-Buy-and-Sell-Stock-with-Cooldown/0309.py)

### 参考

[一个方法团灭 6 道股票问题](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/)