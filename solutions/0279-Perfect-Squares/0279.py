class Solution:
    def numSquares(self, n: int) -> int:
        # solution one: BFS
        q = [(n, 0)]
        visited = [False for i in range(n + 1)]  # initialize all False
        visited[n] = True

        while any(q):  # any: if all elements are False, return False, or return True
            num, step = q.pop(0)

            i = 1
            Num = num - i ** 2
            while Num >= 0:
                if Num == 0:
                    return step + 1
                if not visited[Num]:  # not visited
                    q.append((Num, step + 1))
                    visited[Num] = True
                
                i += 1
                Num = num - i ** 2
        
        # solution two: Lagrange's Four-square Theorem
        while n % 4 == 0:  # reduce n
            n /= 4

        if n % 8 == 7:
            return 4

        a = 0
        while a ** 2 <= n:
            b = int((n - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == n:
                return (not not a) + (not not b)  # whether a and b are positive integers
            a += 1

        return 3

if __name__ == "__main__":
    n = 13
    print(Solution().numSquares(n))