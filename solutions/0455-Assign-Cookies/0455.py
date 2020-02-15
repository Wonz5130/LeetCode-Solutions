class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 贪心
        cnt = 0
        g, s = sorted(g), sorted(s)  # 从小到大排序
        i, j = len(g)-1, len(s)-1  # 指向末尾
        while min(i, j) >= 0:
            if g[i] <= s[j]:  # 贪婪指数要 <= 饼干大小
                cnt += 1
                j -= 1
            i -= 1  # 不管满不满足 size，i 都要往左移一位
        return cnt

if __name__ == "__main__":
    g = [1,2,3]
    s = [1,1]
    print(Solution().findContentChildren(g, s))