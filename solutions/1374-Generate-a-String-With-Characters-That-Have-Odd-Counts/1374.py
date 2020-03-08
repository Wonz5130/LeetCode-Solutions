class Solution:
    def generateTheString(self, n: int) -> str:
        res = []
        if n % 2 == 0:
            for i in range(n-1):
                res.append('a')
            res.append('b')
        else:
            for i in range(n):
                res.append('a')
        return ''.join(res)

if __name__ == "__main__":
    n = 4
    print(Solution().generateTheString(n))  