> LeetCode 0435. Non-overlapping Intervals无重叠区间【Medium】【Python】【区间贪心】

### Problem

[LeetCode](https://leetcode.com/problems/non-overlapping-intervals/)

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

**Example 1:**

```
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
```

**Example 2:**

```
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
```

**Example 3:**

```
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

**Note:**

1. You may assume the interval's end point is always bigger than its start point.
2. Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

### 问题

[力扣](https://leetcode-cn.com/problems/non-overlapping-intervals/)

给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

**示例 1:**

```
输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
```

**示例 2:**

```
输入: [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
```

**示例 3:**

```
输入: [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
```

**注意:**

1. 可以认为区间的终点总是大于它的起点。
2. 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

### 思路

**区间贪心**

先按左端点从小到大排序，然后 temp_pos 指针指向 i 区间，当 temp_pos 指针指向的区间右端点 > i 区间左端点，并且 temp_pos 指针指向的区间右端点 > i 区间右端点时，表示当前区间覆盖范围大于 i 区间，因此可以去掉当前区间，保留 i 区间，更新 temp_pos 指针。只要当 temp_pos 指针指向的区间右端点 > i 区间左端点都要计数+1。当当前区间右端点 <= i 区间左端点，表示不重叠，要更新 temp_pos。

**时间复杂度:** O(len(intervals))

**空间复杂度:** O(1)

### Python代码

```python
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals or len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x[0])  # 按左端点从小到大排序
        temp_pos = 0
        cnt = 0
        for i in range(1, len(intervals)):
            if intervals[temp_pos][1] > intervals[i][0]:  # 当当前区间右端点>i区间左端点
                if intervals[i][1] < intervals[temp_pos][1]:  # 当i区间右端点<当前区间右端点，表示i区间被覆盖在当前区间中
                    temp_pos = i  # 更新temp_pos，选择覆盖范围小的i区间
                cnt += 1  # 当前区间右端点>i区间左端点都要计数+1
            else:
                temp_pos = i  # 当当前区间右端点<=i区间左端点，表示不重叠，要更新temp_pos
        return cnt
```

### 题外话

网上搜的别人的题解发现代码运行都有问题，总是提示：'list' object has no attribute 'start' 等错误。研究了一下，发现网上题解的代码开头都是：

```python
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
```

而现在(2020.02.16)此题的代码开头是：

```python
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
```

该 intervals 是一个二维列表，没有 start，要按照二维列表来做。照着 `LeetCode-0452-用最少数量的箭引爆气球` 自己写的[题解](https://wonzwang.blog.csdn.net/article/details/104347754)，稍微改一下代码发现就能 AC 这道题了。

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0435-Non-overlapping-Intervals/0435.py)