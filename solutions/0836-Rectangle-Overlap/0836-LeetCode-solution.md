> LeetCode 0836. Rectangle Overlap矩形重叠【Easy】【Python】【数学】

### Problem

[LeetCode](https://leetcode.com/problems/rectangle-overlap/)

A rectangle is represented as a list `[x1, y1, x2, y2]`, where `(x1, y1)` are the coordinates of its bottom-left corner, and `(x2, y2)` are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

**Example 1:**

```
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
```

**Example 2:**

```
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
```

**Notes:**

1. Both rectangles `rec1` and `rec2` are lists of 4 integers.
2. All coordinates in rectangles will be between `-10^9 `and` 10^9`.

### 问题

[力扣](https://leetcode-cn.com/problems/rectangle-overlap/)

矩形以列表 `[x1, y1, x2, y2]` 的形式表示，其中 `(x1, y1)` 为左下角的坐标，`(x2, y2)` 是右上角的坐标。

如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。

给出两个矩形，判断它们是否重叠并返回结果。

**示例 1：**

```
输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true
```

**示例 2：**

```
输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
输出：false
```

**提示：**

1. 两个矩形 `rec1` 和 `rec2` 都以含有四个整数的列表的形式给出。
2. 矩形中的所有坐标都处于 `-10^9` 和 `10^9` 之间。
3. `x` 轴默认指向右，`y` 轴默认指向上。
4. 你可以仅考虑矩形是正放的情况。

### 思路

**数学**

```
rec1 = [x1, y1, x2, y2], rec2 = [x3, y3, x4, y4]
max(x1, x3) < x < min(x2, x4)
max(y1, y3) < y < min(y2, y4)
```

##### Python3代码

```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 左下角取 max
        x1 = max(rec1[0], rec2[0])
        y1 = max(rec1[1], rec2[1])
        # 右上角取 min
        x2 = min(rec1[2], rec2[2])
        y2 = min(rec1[3], rec2[3])
       
       # 判断是否重叠
        if x1 < x2 and y1 < y2:
            return True
        else:
            return False
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0836-Rectangle-Overlap/0836.py)