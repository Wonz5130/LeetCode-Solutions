class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def getTime(piles: List[int], speed: int) -> int:
            time = 0
            for pile in piles:
                time += (pile + speed - 1) // speed # 如果是用 >>，注意整除 2 是右移一位
            return time

        while left < right:
            speed = (left + right) >> 1
            time = getTime(piles, speed)
            if time <= h:
                right = speed
            else:
                left = speed + 1
        return left