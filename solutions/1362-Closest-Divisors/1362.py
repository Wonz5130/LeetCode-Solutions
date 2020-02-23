import math
from typing import List

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        num1, num2 = num + 1, num + 2
        ans1 = self.crack(num1)
        ans2 = self.crack(num2)
        res = []
        if abs(ans1 - int(num1 / ans1)) < abs(ans2 - int(num2 / ans2)):  # int
            res.append(ans1)
            res.append(int(num1 / ans1))
            return res
        else:
            res.append(ans2)
            res.append(int(num2 / ans2))
            return res
    
    # calculate factor
    def crack(self, integer):
        factor1, factor2 = 1, integer
        for i in range(1, int(math.sqrt(integer)) + 1):  # range: [1, sqrt(x) + 1)
            if int(integer / i) == integer / i:  # i is factor
                if integer / i - i < factor2 - factor1:
                    factor1, factor2 = i, integer / i
        return factor1

if __name__ == "__main__":
    num = 123
    print(Solution().closestDivisors(num))