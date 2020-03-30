class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n < 1 or m < 1:
            return None
            
        last = 0
        # 最后一轮只剩两个人，倒过来推
        for i in range(2, n + 1):
            last = (last + m) % i
        return last