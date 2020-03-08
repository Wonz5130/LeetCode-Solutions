> LeetCode 1370. Increasing Decreasing String上升下降字符串【Easy】【Python】【排序】

### Problem

[LeetCode](https://leetcode.com/problems/increasing-decreasing-string/)

Given a string `s`. You should re-order the string using the following algorithm:

1. Pick the **smallest** character from `s` and **append** it to the result.
2. Pick the **smallest** character from `s` which is greater than the last appended character to the result and **append** it.
3. Repeat step 2 until you cannot pick more characters.
4. Pick the **largest** character from `s` and **append** it to the result.
5. Pick the **largest** character from `s` which is smaller than the last appended character to the result and **append** it.
6. Repeat step 5 until you cannot pick more characters.
7. Repeat the steps from 1 to 6 until you pick all characters from `s`.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return *the result string* after sorting `s` with this algorithm.

**Example 1:**

```
Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
```

**Example 2:**

```
Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
```

**Example 3:**

```
Input: s = "leetcode"
Output: "cdelotee"
```

**Example 4:**

```
Input: s = "ggggggg"
Output: "ggggggg"
```

**Example 5:**

```
Input: s = "spo"
Output: "ops"
```

**Constraints:**

- `1 <= s.length <= 500`
- `s` contains only lower-case English letters.

### 问题

[力扣](https://leetcode-cn.com/problems/increasing-decreasing-string/)

给你一个字符串 s ，请你根据下面的算法重新构造字符串：

1. 从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
2. 从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
3. 重复步骤 2 ，直到你没法从 s 中选择字符。
4. 从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
5. 从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
6. 重复步骤 5 ，直到你没法从 s 中选择字符。
7. 重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。

在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

请你返回将 s 中字符重新排序后的 **结果字符串** 。

**示例 1：**

```
输入：s = "aaaabbbbcccc"
输出："abccbaabccba"
解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"
```

**示例 2：**

```
输入：s = "rat"
输出："art"
解释：单词 "rat" 在上述算法重排序以后变成 "art"
```

**示例 3：**

```
输入：s = "leetcode"
输出："cdelotee"
```

**示例 4：**

```
输入：s = "ggggggg"
输出："ggggggg"
```

**示例 5：**

```
输入：s = "spo"
输出："ops"
```

**提示：**

* `1 <= s.length <= 500`
* `s` 只包含小写英文字母。

### 思路

**排序**

```
对字符串进行排序，然后一遍递增，一遍递减，逐步加入到 res 中，直到 s 为空。
```

**空间复杂度:** O(len(s))

##### Python3代码

```python
class Solution:
    def sortString(self, s: str) -> str:
        if not s:
            return ''
        
        s = list(s)
        res = []
        while s:
            # increasing: 递增
            temp_list = list(set(s))  # set可以去重
            temp_list.sort(key=lambda c: ord(c))  # ord()：转化ASCII字符为相应的数字
            for i in temp_list:
                res.append(i)
                s.remove(i)
            
            # decreasing: 递减
            temp_list = list(set(s))
            temp_list.sort(key=lambda c: ord(c), reverse=True)
            for i in temp_list:
                res.append(i)
                s.remove(i)
        return ''.join(res)
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1370-Increasing-Decreasing-String/1370.py)