> LeetCode 0452. Minimum Number of Arrows to Burst Balloons用最少数量的箭引爆气球【Medium】【Python】【区间贪心】

### Problem

[LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 10^4 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

**Example:**

```
Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
```

### 问题

[力扣](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/)

在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在10^4个气球。

一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

**Example:**

```
输入:
[[10,16], [2,8], [1,6], [7,12]]

输出:
2

解释:
对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。
```

### 思路

**区间贪心**

先把右端点从小到大排序，然后 temp_pos 指针指向第一组右端点，每次都是比较 temp_pos 和当前的左端点，如果 temp_pos < 左端点时，表明需要再加一支箭，然后更新 temp_pos 为当前的右端点，继续比较。

**时间复杂度**: O(len(points))
**空间复杂度**: O(1)

### Python代码

```python
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points or len(points) == 0:
            return 0
        points.sort(key = lambda x: x[1])  # 按右端点从小到大排序
        temp_pos = points[0][1]
        cnt = 1
        for i in range(len(points)):
            if temp_pos >= points[i][0]:  # 当右端点<左端点时，要再加一支箭
                continue
            temp_pos = points[i][1]
            cnt += 1
        return cnt
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0452-Minimum-Number-of-Arrows-to-Burst-Balloons/0452.py)