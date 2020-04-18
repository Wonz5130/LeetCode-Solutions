class Solution:
    def minCount(self, coins: List[int]) -> int:
        cnt = 0
        for x in coins:
            if x % 2:
                cnt += (x // 2 + 1)
            else:
                cnt += x // 2
        return cnt