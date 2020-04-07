class Solution:
    def hammingWeight(self, n: int) -> int:
        # solution one
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

        # solution two
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res