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
                
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))