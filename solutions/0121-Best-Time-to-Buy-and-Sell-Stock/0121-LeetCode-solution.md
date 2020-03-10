> LeetCode 0121. Best Time to Buy and Sell Stock买卖股票的最佳时机【Easy】【Python】【贪心】【动态规划】

### Problem

[LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

**Example 1:**

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

**Example 2:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

### 问题

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

**示例 1:**

```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```

**示例 2:**

```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

### 思路

##### 解法一

**贪心**

```
买入和卖出同时计算。
当 buy > price，更新买入价格 buy。
当 profit < price - buy，更新利润 profit。
```

**时间复杂度:** O(len(prices))
**空间复杂度:** O(1)

### Python3代码

```python
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
```

##### 解法二

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

k = 1
所以 dp[i-1][1][0] = 0
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
dp[i][1][1] = max(dp[i-1][1][1], -prices[i])

k 都是 1，所以 k 对状态转移没有影响：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], -prices[i])

i = 0 时，dp[i-1] 不合法。
dp[0][0] = max(dp[-1][0], dp[-1][1] + prices[i])
         = max(0, -infinity + prices[i])
         = 0
dp[0][1] = max(dp[-1][1], dp[-1][0] - prices[i])
         = max(-infinity, 0 - prices[i]) 
         = -prices[i]
```

**空间复杂度:** O(1)

### Python3代码

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0121-Best-Time-to-Buy-and-Sell-Stock/0121.py)