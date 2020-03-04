from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # solution one: backtracking
        ans = []
        self.dfs(s, [], ans)
        return ans
    
    def dfs(self, s, path, ans):
        if len(s) > (4 - len(path)) * 3:  # pruning: len(s) > 12
            return
        if not s and len(path) == 4:  # remove first '.' and IP address should be 4 parts
            ans.append('.'.join(path))
            return
        for i in range(min(3, len(s))):
            cur = s[:i + 1]
            if(cur[0] == '0' and len(cur) >= 2) or int(cur) > 255:  # invalid IP address
                continue
            self.dfs(s[i + 1:], path + [s[:i + 1]], ans)
        
        # solution two: brute force search
        ans = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if a + b + c + d == len(s):
                            ss = [s[:a], s[a:a+b], s[a+b:a+b+c], s[a+b+c:]]
                            flag = 0
                            for k in range(4):
                                if int(ss[k]) > 255:
                                    flag = 1
                                    break
                                if len(ss[k]) >= 2 and ss[k][0] == '0':  # for example: 0xx.xxx.xxx.xxx
                                    flag = 1
                                    break
                            if flag == 0:
                                ans.append(ss[0] + '.' + ss[1] + '.' + ss[2] + '.' + ss[3])
        return ans

if __name__ == "__main__":
    s = "25525511135"
    print(Solution().restoreIpAddresses(s))