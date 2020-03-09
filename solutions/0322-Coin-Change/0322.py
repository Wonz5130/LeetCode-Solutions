from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.res = float("inf")

        def dfs(i, num, amount):
            # 终止情况
            if amount == 0:
                self.res = min(self.res, num)
                return
            for j in range(i, len(coins)):
                # 最大值也不满足
                if (self.res - num) * coins[j] < amount:
                    break
                if coins[j] > amount:
                    continue
                dfs(j, num + 1, amount - coins[j])
            
        for i in range(len(coins)):
            dfs(i, 0, amount)
        
        return self.res if self.res != float("inf") else -1

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins, amount))