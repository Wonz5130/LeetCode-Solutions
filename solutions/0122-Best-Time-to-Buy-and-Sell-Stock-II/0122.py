class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 0:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            if(prices[i+1] > prices[i]):
                profit += prices[i+1] - prices[i]
        return profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))