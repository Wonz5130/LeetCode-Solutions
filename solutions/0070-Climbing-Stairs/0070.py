class Solution:
    def climbStairs(self, n: int) -> int:
        # 初始条件和斐波那契数列有区别
        dp_0, dp_1 = 1, 1
        for _ in range(n):
            dp_0, dp_1 = dp_1, dp_0 + dp_1
        return dp_0