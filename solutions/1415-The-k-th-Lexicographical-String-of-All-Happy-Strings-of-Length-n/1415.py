class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        happy = ['a', 'b', 'c']

        def dfs(curr, temp):
            # 剪枝，后面的不需要了
            if len(res) == k:
                return
            # 长度为 n，满足条件
            if len(curr) == n:
                res.append(curr)
                return
            # 长度不到就从 happy 里再选字符
            for x in temp:
                temp = []
                # 选择跟前一个字符不同的字符
                for c in happy:
                    if c != x:
                        temp.append(c)
                # temp = [c for c in happy if c != x]
                # print(temp)
                dfs(curr + x, temp)
        
        dfs('', happy)
        # print(len(res))
        return res[-1] if len(res) == k else ''

if __name__ == "__main__":
    n = 3
    k = 9
    print(Solution().getHappyString(n, k))