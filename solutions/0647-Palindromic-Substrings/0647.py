class Solution:
    def countSubstrings(self, s: str) -> int:
        # solution one: 中心拓展
        n = len(s)
        ans = 0
        for i in range(2 * n - 1):
            left, right = int(i / 2), int(i / 2) + i % 2
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1 # 往左移
                right += 1 # 往右移
                ans += 1
        return ans

        # solution two: 动态规划
        if s is None or s == "":
            return 0
        
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = len(s)

        for i in range(n):
            # base case
            dp[i][i] = True
        # 从左下方往上遍历
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # i和j相邻，即回文子串长度为2
                    if j - i == 1:
                        dp[i][j] = True
                    # 除去左右两头，剩下的substring是不是回文子串
                    else:
                        dp[i][j] =  dp[i + 1][j - 1]
                # 不相等就不是回文子串
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    res += 1
        return res

if __name__ == "__main__":
    s = "aaa"
    print(Solution().countSubstrings(s))