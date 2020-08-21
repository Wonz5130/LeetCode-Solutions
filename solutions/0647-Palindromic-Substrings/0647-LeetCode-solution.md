> LeetCode 0647. Palindromic Substrings回文子串【Medium】【Python】【中心扩展】【动态规划】

### Problem

[LeetCode](https://leetcode.com/problems/palindromic-substrings/)

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

**Example 1:**

```
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

**Example 2:**

```
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

**Note:**

1. The input string length won't exceed 1000.

### 问题

[力扣](https://leetcode-cn.com/problems/palindromic-substrings/)

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

**示例 1：**

```
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
```

**示例 2：**

```
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
```

**提示：**

* 输入的字符串长度不会超过 1000 。

### 思路

##### 解法一：中心拓展

```
枚举每一个可能的回文中心，双指针分别向两边拓展，指针指向元素相同就继续拓展。
因为要考虑回文长度是奇数还是偶数，为减少时间复杂度，故选择用一个循环解决。
```

举例 n = 4：

| 编号i | 回文中心左起始位置 *li* | 回文中心右起始位置 *ri* |
| ----- | ----------------------- | ----------------------- |
| 0     | 0                       | 0                       |
| 1     | 0                       | 1                       |
| 2     | 1                       | 1                       |
| 3     | 1                       | 2                       |
| 4     | 2                       | 2                       |
| 5     | 2                       | 3                       |
| 6     | 3                       | 3                       |

```
经过分析，长度为 n 的字符串会生成 2n-1 组回文中心[li,ri]，其中li = i/2，ri = li + (i mod 2)。
只需遍历 0 到 2n-2，就找到了所有的回文中心。
```

**时间复杂度:** O(n^2)

##### Python3代码

```python
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
```

##### 解法二：动态规划

```
字符串 dp[i...j] 是否为回文串，如果是，dp[i][j] = true，如果不是，dp[i][j] = false

动态转移方程：dp[i][j] = dp[i + 1][j - 1]

base case：只有一个字母的时候肯定是回文子串

先判断左右两头是否相同：
	相同：
		j - i == 1：表示子串长度为2
		j - i != 1：判断除去左右两头，剩下的 substring 是不是回文子串
	不同：
		不是回文子串
```

**时间复杂度:** O(n^2)

##### Python3代码

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        # solution two: 动态规划
        if s is None or s == "":
            return 0
        
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = len(s)

        for i in range(n):
            # base case
            dp[i][i] = True
        # 从左往右上遍历右边一个三角区域
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # i 和 j 相邻，即回文子串长度为2
                    if j - i == 1:
                        dp[i][j] = True
                    # 除去左右两头，剩下的 substring 是不是回文子串
                    else:
                        dp[i][j] =  dp[i + 1][j - 1]
                # 不相等就不是回文子串
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    res += 1
        return res
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0647-Palindromic-Substrings/0647.py)

### 参考

[回文子串](https://leetcode-cn.com/problems/palindromic-substrings/solution/hui-wen-zi-chuan-by-leetcode-solution/)

[647. 回文子串 动态规划方式求解](https://leetcode-cn.com/problems/palindromic-substrings/solution/647-hui-wen-zi-chuan-dong-tai-gui-hua-fang-shi-qiu/)