class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # FibonacciNumbers
        def fib(num):
            a, b = 0, 1
            res = []
            while b <= num:
                res.append(b)
                a, b = b, a + b
            return res
        
        num = fib(k)
        cnt = 0
        while k:
            if k >= num[-1]:
                k -= num[-1]
                cnt += 1
            else:
                num.pop()
        return cnt

if __name__ == "__main__":
    k = 19
    print(Solution().findMinFibonacciNumbers(k))