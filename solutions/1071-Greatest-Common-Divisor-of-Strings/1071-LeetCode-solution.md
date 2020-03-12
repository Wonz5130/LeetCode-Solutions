> LeetCode 1071. Greatest Common Divisor of Strings字符串的最大公因子【Easy】【Python】【字符串】

### Problem

[LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

For strings `S` and `T`, we say "`T` divides `S`" if and only if `S = T + ... + T` (`T` concatenated with itself 1 or more times)

Return the largest string `X` such that `X` divides str1 and `X` divides str2.

**Example 1:**

```
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```

**Example 2:**

```
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
```

**Example 3:**

```
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

**Note:**

1. `1 <= str1.length <= 1000`
2. `1 <= str2.length <= 1000`
3. `str1[i]` and `str2[i]` are English uppercase letters.

### 问题

[力扣](https://leetcode-cn.com/problems/greatest-common-divisor-of-strings/)

对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

**示例 1：**

```
输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
```

**示例 2：**

```
输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
```

**示例 3：**

```
输入：str1 = "LEET", str2 = "CODE"
输出：""
```

**提示：**

1. `1 <= str1.length <= 1000`
2. `1 <= str2.length <= 1000`
3. `str1[i]` 和 `str2[i]` 为大写英文字母

### 思路

**字符串**

##### 解法一

```
str1 和 str2 逐个字符比较，不相等就返回 ""。
相等，就求 m, n 的最大公约数，返回 str1 中从头到最大公约数位置的字符串。（左闭右开）
```

**时间复杂度:** O(max(m, n))，m 是 str1 的长度，n 是 str2 的长度。
**空间复杂度:** O(log(min(m, n)))，m 是 str1 的长度，n 是 str2 的长度。

##### Python3代码

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        # solution one
        i, j = 0, 0
        while i < m or j < n:
            if str1[i % m] != str2[j % n]:
                return ""
            i += 1
            j += 1
        
        # 求最大公约数
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        
        return str1[:gcd(m, n)]

if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"
    print(Solution().gcdOfStrings(str1, str2))
```

##### 解法二

```
直接比较 str1 + str2 是否等于 str2 + str1，不相等就返回 ""。
相等，就求 m, n 的最大公约数，返回 str1 中从头到最大公约数位置的字符串。（左闭右开）
```

**时间复杂度:** O(m + n)，m 是 str1 的长度，n 是 str2 的长度。
**空间复杂度:** O(m + n)，m 是 str1 的长度，n 是 str2 的长度。

##### Python3代码

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        # solution two
        if str1 + str2 != str2 + str1:
            return ""
        
        # 求最大公约数
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        
        return str1[:gcd(m, n)]

if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"
    print(Solution().gcdOfStrings(str1, str2))
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1071-Greatest-Common-Divisor-of-Strings/1071.py)