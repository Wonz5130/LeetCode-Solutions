> LeetCode 1394. Find Lucky Integer in an Array找出数组中的幸运数【Easy】【Python】【暴力】

### Problem

[LeetCode](https://leetcode.com/problems/find-lucky-integer-in-an-array/)

Given an array of integers `arr`, a lucky integer is an integer which has a frequency in the array equal to its value.

Return *a lucky integer* in the array. If there are multiple lucky integers return the **largest** of them. If there is no lucky integer return **-1**.

**Example 1:**

```
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
```

**Example 2:**

```
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
```

**Example 3:**

```
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.
```

**Example 4:**

```
Input: arr = [5]
Output: -1
```

**Example 5:**

```
Input: arr = [7,7,7,7,7,7,7]
Output: 7
```

**Constraints:**

- `1 <= arr.length <= 500`
- `1 <= arr[i] <= 500`

### 问题

[力扣](https://leetcode-cn.com/problems/find-lucky-integer-in-an-array/)

在整数数组中，如果一个整数的出现频次和它的数值大小相等，我们就称这个整数为「幸运数」。

给你一个整数数组 arr，请你从中找出并返回一个幸运数。

* 如果数组中存在多个幸运数，只需返回 最大 的那个。
* 如果数组中不含幸运数，则返回 -1 。

**示例 1：**

```
输入：arr = [2,2,3,4]
输出：2
解释：数组中唯一的幸运数是 2 ，因为数值 2 的出现频次也是 2 。
```

**示例 2：**

```
输入：arr = [1,2,2,3,3,3]
输出：3
解释：1、2 以及 3 都是幸运数，只需要返回其中最大的 3 。
```

**示例 3：**

```
输入：arr = [2,2,2,3,3]
输出：-1
解释：数组中不存在幸运数。
```

**示例 4：**

```
输入：arr = [5]
输出：-1
```

**示例 5：**

```
输入：arr = [7,7,7,7,7,7,7]
输出：7
```

**提示：**

* `1 <= arr.length <= 500`
* `1 <= arr[i] <= 500`

### 思路

**暴力**

```
自定义排序，然后暴力求解。
```

##### Python3代码

```python
from typing import List
import collections

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        # 先按频次排序，再按数值大小排序
        res = sorted(cnt.items(), key=lambda x:(x[1],x[0]), reverse=True)
        for i in range(len(res)):
            # 频次等于数值大小
            if res[i][0] == res[i][1]:
                return res[i][0]
        return -1
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1394-Find-Lucky-Integer-in-an-Array/1394.py)