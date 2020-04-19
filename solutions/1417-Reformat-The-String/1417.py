class Solution:
    def reformat(self, s: str) -> str:
        n = len(s)
        s = list(s)
        # print(s)
        num, ss = [], []
        for i in range(n):
            # 字符
            if 'a' <= s[i] <= 'z':
                ss.append(s[i])
            # 数字
            else:
                num.append(s[i])
        # 当字符数组长度和数字数组长度相差大于1，肯定不满足
        if abs(len(num) - len(ss)) > 1:
            return ""
        else:
            res = []
            # 数字多，先数字
            if len(num) > len(ss):
                for i in range(len(ss)):
                    res.append(num[i])
                    res.append(ss[i])
                res.append(num[-1])
            # 字符多，先字符
            elif len(num) < len(ss):
                for i in range(len(num)):
                    res.append(ss[i])
                    res.append(num[i])
                res.append(ss[-1])
            # 一样多
            else:
                for i in range(len(ss)):
                    res.append(num[i])
                    res.append(ss[i])
        # 最后要将列表转化为字符串
        return ''.join(res)

if __name__ == "__main__":
    s = "a0b1c2"
    print(Solution().reformat(s))