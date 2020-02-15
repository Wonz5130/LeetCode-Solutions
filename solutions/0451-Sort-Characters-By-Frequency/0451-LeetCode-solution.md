> LeetCode 0451. Sort Characters By Frequency根据字符出现频率排序【Medium】【Python】【桶排序】

### Problem

[LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/submissions/)

Given a string, sort it in decreasing order based on the frequency of characters.

**Example 1:**

```
Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

**Example 2:**

```
Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
```

**Example 3:**

```
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

### 问题

[力扣](https://leetcode-cn.com/problems/sort-characters-by-frequency/submissions/)

给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

**示例 1:**

```
输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
```

**示例 2:**

```
输入:
"cccaaa"

输出:
"cccaaa"

解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
```

**示例 3:**

```
输入:
"Aabb"

输出:
"bbAa"

解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
```

### 思路

**桶排序**

统计字符串字符出现的次数，然后桶排序，最后逆序输出字符串。

可以直接用 Python 的Counter类就能统计每个字符出现的次数，使用most_common函数就能按次序排列。

**时间复杂度**: O(n)
**空间复杂度**: O(m)  m是桶的数量

### Python代码

```python
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # 法一：collections.Counter
        # import collections  # 需要导入collections
        # count = collections.Counter(s).most_common()  # Counter类就能统计每个字符出现的次数, 使用most_common函数就能按次序排列
        # res = ''
        # for char, cnt in count:
        #     res += char*cnt  # 字符与次数相乘
        # return res
        
        # 法二：桶排序
        import collections

        # 统计字符个数
        ret = []
        count_frequency = collections.defaultdict(int)
        for i in s:
            count_frequency[i] += 1  # 统计字符个数
        
        # 桶排序
        buckets = [[] for i in range(len(s) + 1)]
        for i in count_frequency:  # i是字符
            # print (i)
            buckets[count_frequency[i]].extend(i * count_frequency[i])
        
        # 打印排完序的字符串
        for i in buckets[::-1]:  # -1表示逆序
            if(i):
                ret.extend(i)
        return ''.join(ret)

        # return ''.join(c*-n for n,c in sorted((-s.count(c),c)for c in set(s)))  # 一行代码也能解决
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0451-Sort-Characters-By-Frequency/0451.py)