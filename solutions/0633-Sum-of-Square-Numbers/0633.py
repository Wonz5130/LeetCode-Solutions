class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        b = int(c**0.5)+1
        while a <= b:  # 假如 c = 2, 发现不加 = , 输出 False, 应该输出 True
            if a*a + b*b == c:
                return True
            elif a*a + b*b < c:
                a += 1
            else:
                b -= 1
        return False

if __name__ == "__main__":
    c = 5
    print(Solution().judgeSquareSum(c))