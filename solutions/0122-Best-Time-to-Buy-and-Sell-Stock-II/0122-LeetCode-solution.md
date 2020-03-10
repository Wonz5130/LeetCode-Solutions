> LeetCode 0122. Best Time to Buy and Sell Stock II买卖股票的最佳时机 II【Easy】【Python】【贪心】【动态规划】

### Problem

[LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

**Note:** You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

**Example 1:**

```
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 			  3.
```

**Example 2:**

```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you 			  are engaging multiple transactions at the same time. You must sell before  			  buying again.
```

**Example 3:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

### 问题

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

**注意:** 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例 1:**

```
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
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
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

### 思路

##### 解法一

**贪心**

```
根据题意，是按照每天的顺序进行股票买入与卖出。
于是，只要后一天价格大于前一天价格，就可买入卖出这只股票。
```

**时间复杂度:** O(len(prices))
**空间复杂度:** O(1)

##### Python3代码

```python
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

k = +inf
因为 k 为正无穷，那么可以把 k 和 k-1 看成是一样的。
buy+sell = 一次完整的交易，这里把 sell 看成一次交易，所以第一行是 k-1。
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k-1][1] + prices[i])
			= max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])

所以 k 对状态转移没有影响：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

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
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0122-Best-Time-to-Buy-and-Sell-Stock-II/0122.py)

### 参考

[一个方法团灭 6 道股票问题](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/)