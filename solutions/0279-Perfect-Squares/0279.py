class Solution:
    def numSquares(self, n: int) -> int:
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

if __name__ == "__main__":
    n = 13
    print(Solution().numSquares(n))