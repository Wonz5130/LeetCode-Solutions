> LeetCode 1358. Number of Substrings Containing All Three Characters包含所有三种字符的子字符串数目【Medium】【Python】【双指针】【滑窗】

### Problem

[LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)

Given a string `s` consisting only of characters *a*, *b* and *c*.

Return the number of substrings containing **at least** one occurrence of all these characters *a*, *b* and *c*.

**Example 1:**

```
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
```

**Example 2:**

```
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
```

**Example 3:**

```
Input: s = "abc"
Output: 1
```

**Constraints:**

- `3 <= s.length <= 5 x 10^4`
- `s` only consists of *a*, *b* or *c* characters.

### 问题

[力扣](https://leetcode-cn.com/problems/number-of-substrings-containing-all-three-characters/)

给你一个字符串 `s` ，它只包含三种字符 a, b 和 c 。

请你返回 a，b 和 c 都 **至少** 出现过一次的子字符串数目。

**示例 1：**

```
输入：s = "abcabc"
输出：10
解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
```

**示例 2：**

```
输入：s = "aaacb"
输出：3
解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
```

**示例 3：**

```
输入：s = "abc"
输出：1
```

**提示：**

* `3 <= s.length <= 5 x 10^4`
* `s` 只包含字符 a，b 和 c 。

### 思路

**双指针** **滑动窗口**

```
1. 如果窗口内有 a, b, c, 那么窗口继续向右拉开都满足
2. 如果窗口内没有 a, b, c, 那么 right 指针右移找到满足窗口内有 a,  b, c
3. 然后 left 指针右移，每次都要判断上面两种情况
```

**时间复杂度:** O(n)
**空间复杂度:** O(n)

### Python3代码

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if len(s) <= 2:
            return 0
        length = len(s)
        left, right = 0, 2
        ans = 0
        while left < length - 2:
            window = s[left: right + 1]  # [left, right + 1)
            if 'a' in window and 'b' in window and 'c' in window:
                ans += length - right  # if s[left: right + 1] satisfies, then s[left: length] also satisfies
                left += 1  # move left
            else:
                right += 1  # move right
                if right == length:  # s[left: length] does not satisfy, so s[left + x: length] also does not satisfy
                    break
        return ans
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1358-Number-of-Substrings-Containing-All-Three-Characters/1358.py)