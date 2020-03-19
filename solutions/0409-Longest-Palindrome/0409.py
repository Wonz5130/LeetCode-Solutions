class Solution:
    def longestPalindrome(self, s: str) -> int:
        import collections
        # 统计各字符个数
        count = collections.Counter(s).values()
        sum = 0
        for x in count:
            if x // 2 > 0:
                # 取偶数个字符
                sum += x // 2 * 2
        if sum == len(s):
            return sum
        else:
            return sum + 1