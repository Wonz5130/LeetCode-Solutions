> LeetCode 0093. Restore IP Addresses复原IP地址【Medium】【Python】【回溯】【DFS】【暴力】

### Problem

[LeetCode](https://leetcode.com/problems/restore-ip-addresses/)

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

**Example:**

```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

### 问题

[力扣](https://leetcode-cn.com/problems/restore-ip-addresses/)

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

**示例:**

```
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
```

### 思路

##### 解法一

**回溯 DFS**

```
回溯算法的关键就是合理剪枝，这个也是难点。
详细可以看代码注释。
```

下面剪枝图片来源于 [liweiwei1419](https://leetcode-cn.com/u/liweiwei1419/) 的 [回溯算法（画图分析剪枝条件）](https://leetcode-cn.com/problems/restore-ip-addresses/solution/hui-su-suan-fa-hua-tu-fen-xi-jian-zhi-tiao-jian-by/)

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/Snipaste_2020-03-04_20-22-30.png)

##### Python3代码

```python
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
```

##### 解法二

**暴力**

```
暴力出奇迹
四次 for 遍历，再分别取四部分作为地址，分别判断是否合法。
最后拼接一下，加入 ans 中。
```

##### Python3代码

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
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
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0093-Restore-IP-Addresses/0093.py)

### 参考

[【LeetCode】93. Restore IP Addresses 解题报告（Python & C++）](https://blog.csdn.net/fuxuemingzhu/article/details/80657420)

[LeetCode-93-Restore IP Addresses 暴力](https://blog.csdn.net/qdbszsj/article/details/78165372)