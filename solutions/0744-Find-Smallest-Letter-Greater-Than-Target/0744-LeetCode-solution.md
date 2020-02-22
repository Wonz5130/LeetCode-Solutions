> LeetCode 0744. Find Smallest Letter Greater Than Target寻找比目标字母大的最小字母【Easy】【Python】【二分】

### Problem

[LeetCode](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)

Given a list of sorted characters `letters` containing only lowercase letters, and given a target letter `target`, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is `target = 'z'` and `letters = ['a', 'b']`, the answer is `'a'`.

**Examples:**

```
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
```

**Note:**

1. `letters` has a length in range `[2, 10000]`.
2. `letters` consists of lowercase letters, and contains at least 2 unique letters.
3. `target` is a lowercase letter.

### 问题

[力扣](https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/)

给定一个只包含小写字母的有序数组 `letters` 和一个目标字母 `target`，寻找有序数组里面比目标字母大的最小字母。

数组里字母的顺序是循环的。举个例子，如果目标字母 `target = 'z'` 并且有序数组为 `letters = ['a', 'b']`，则答案返回 `'a'`。

**示例:**

```
输入:
letters = ["c", "f", "j"]
target = "a"
输出: "c"

输入:
letters = ["c", "f", "j"]
target = "c"
输出: "f"

输入:
letters = ["c", "f", "j"]
target = "d"
输出: "f"

输入:
letters = ["c", "f", "j"]
target = "g"
输出: "j"

输入:
letters = ["c", "f", "j"]
target = "j"
输出: "c"

输入:
letters = ["c", "f", "j"]
target = "k"
输出: "c"
```

**注:**

1. `letters` 长度范围在 `[2, 10000]` 区间内。
2. `letters` 仅由小写字母组成，最少包含两个不同的字母。
3. 目标字母 `target` 是一个小写字母。

### 思路

**二分查找**

注意数组是循环的，所以如果 target >= 最后一个字母，直接返回 letters[0] 即可。

**时间复杂度:** O(logn)
**空间复杂度:** O(1)

### Python代码

```python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low, high = 0, len(letters) - 1
        while low <= high:
            mid = int((low + high) / 2)  # element in list must be int
            if letters[mid] <= target:
                low = mid + 1
            else:
                if mid < 1 or (mid >= 1 and letters[mid-1] <= target):
                    return letters[mid]
                high = mid - 1
        return letters[0]  # 'z' < 'a'
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0744-Find-Smallest-Letter-Greater-Than-Target/0744.py)