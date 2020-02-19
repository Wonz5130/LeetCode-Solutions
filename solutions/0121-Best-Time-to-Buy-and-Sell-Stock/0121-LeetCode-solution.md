> LeetCode 0121. Best Time to Buy and Sell Stock买卖股票的最佳时机【Easy】【Python】【贪心】

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

**贪心**

买入和卖出同时计算，当 buy > price，更新买入价格 buy，当 profit < price - buy，更新利润 profit。

**时间复杂度:** O(len(prices))
**空间复杂度:** O(1)

### Python代码

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit, buy = 0, 0x7FFFFFFF
        for price in prices:
            if buy > price:
                buy = price  # 尽量买入价格小的股票
            if profit < price - buy:
                profit = price - buy  # 尽量在最大价格卖出股票
        return profit
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0121-Best-Time-to-Buy-and-Sell-Stock/0121.py)