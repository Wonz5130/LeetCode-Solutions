from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.dfs(s, [], ans)
        return ans
    
    def dfs(self, s, path, ans):
        if len(s) > (4 - len(path)) * 3:  # pruning
            return
        if not s and len(path) == 4:
            ans.append('.'.join(path))
            return
        for i in range(min(3, len(s))):
            cur = s[:i + 1]
            if(cur[0] == '0' and len(cur) >= 2) or int(cur) > 255:  # invalid IP address
                continue
            self.dfs(s[i + 1:], path + [s[:i + 1]], ans)

if __name__ == "__main__":
    s = "25525511135"
    print(Solution().restoreIpAddresses(s))