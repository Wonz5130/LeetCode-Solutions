from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        import collections
        import math
        # Counter统计出来是一个字典
        c = list(collections.Counter(deck).values())
        res = c[0]
        # 求所有数的最大公约数
        for x in c:
            res = math.gcd(res, x)
        return res > 1

if __name__ == "__main__":
    deck = [1,2,3,4,4,3,2,1]
    print(Solution().hasGroupsSizeX(deck))