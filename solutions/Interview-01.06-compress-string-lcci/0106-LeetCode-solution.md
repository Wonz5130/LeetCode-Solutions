> LeetCode 面试题 01.06. 字符串压缩【Easy】【Python】【双指针】

### 问题

[力扣](https://leetcode-cn.com/problems/compress-string-lcci/)

字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

**示例1:**

```
 输入："aabcccccaaa"
 输出："a2b1c5a3"
```

**示例2:**

```
 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
```

**提示：**

1. 字符串长度在[0, 50000]范围内。

### 思路

**双指针**

```
每次统计相同字符个数，加入到 res 中。
最后比较一下压缩后的长度和原字符串长度，输出短的那个。
```

##### Python3代码

```python
class Solution:
    def compressString(self, S: str) -> str:
        n = len(S)
        res = ''
        i = 0
        while i < n:
            j = i
            while j < n and S[j] == S[i]:
                j += 1
            res += S[i] + str(j - i)
            i = j
        
        if len(res) < n:
            return res
        else:
            return S
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-01.06-compress-string-lcci/0106.py)