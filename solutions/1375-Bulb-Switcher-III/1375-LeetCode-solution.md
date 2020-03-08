> LeetCode 1375. Bulb Switcher III灯泡开关 III【Medium】【Python】【最大编号】

### Problem

[LeetCode](https://leetcode.com/problems/bulb-switcher-iii/)

There is a room with `n` bulbs, numbered from `1` to `n`, arranged in a row from left to right. Initially, all the bulbs are turned off.

At moment *k* (for *k* from `0` to `n - 1`), we turn on the `light[k]` bulb. A bulb **change color to blue** only if it is on and all the previous bulbs (to the left) are turned on too.

Return the number of moments in which **all turned on** bulbs **are blue.**

**Example 1:**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/sample_2_1725.png)

```
Input: light = [2,1,3,5,4]
Output: 3
Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.
```

**Example 2:**

```
Input: light = [3,2,4,1,5]
Output: 2
Explanation: All bulbs turned on, are blue at the moment 3, and 4 (index-0).
```

**Example 3:**

```
Input: light = [4,1,2,3]
Output: 1
Explanation: All bulbs turned on, are blue at the moment 3 (index-0).
Bulb 4th changes to blue at the moment 3.
```

**Example 4:**

```
Input: light = [2,1,4,3,6,5]
Output: 3
```

**Example 5:**

```
Input: light = [1,2,3,4,5,6]
Output: 6
```

**Constraints:**

- `n == light.length`
- `1 <= n <= 5 * 10^4`
- `light` is a permutation of `[1, 2, ..., n]`

### 问题

[力扣](https://leetcode-cn.com/problems/bulb-switcher-iii/)

房间中有 n 枚灯泡，编号从 1 到 n，自左向右排成一排。最初，所有的灯都是关着的。

在 k  时刻（ k 的取值范围是 0 到 n - 1），我们打开 light[k] 这个灯。

灯的颜色要想 **变成蓝色** 就必须同时满足下面两个条件：

* 灯处于打开状态。
* 排在它之前（左侧）的所有灯也都处于打开状态。

请返回能够让 **所有开着的** 灯都 **变成蓝色** 的时刻 **数目** 。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/sample_2_1725.png)

```
输入：light = [2,1,3,5,4]
输出：3
解释：所有开着的灯都变蓝的时刻分别是 1，2 和 4 。
```

**示例 2：**

```
输入：light = [3,2,4,1,5]
输出：2
解释：所有开着的灯都变蓝的时刻分别是 3 和 4（index-0）。
```

**示例 3：**

```
输入：light = [4,1,2,3]
输出：1
解释：所有开着的灯都变蓝的时刻是 3（index-0）。
第 4 个灯在时刻 3 变蓝。
```

**示例 4：**

```
输入：light = [2,1,4,3,6,5]
输出：3
```

**示例 5：**

```
输入：light = [1,2,3,4,5,6]
输出：6
```

**提示：**

- `n == light.length`
- `1 <= n <= 5 * 10^4`
- `light` 是 `[1, 2, ..., n]` 的一个排列。

### 思路

**最大编号**

```
遍历一遍，修改当前状态为开灯，并比较开灯次数是否等于记录的最大编号。
如果相等，表示灯可以变蓝，于是就计数 + 1。
```

**时间复杂度:** O(n)
**空间复杂度:** O(1)

##### Python3代码

```python
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        flag = [False] * (n+1)
        cnt_blue, cnt_light = 0, 0
        max_i = 0
        for i in range(n):
            flag[light[i]] = True  # turn on bulb开灯
            cnt_light += 1
            max_i = max(max_i, light[i])
            # 已开灯数量 = 当前记录的最大编号：灯变蓝计数 + 1
            if cnt_light == max_i:
                cnt_blue += 1
        return cnt_blue
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1375-Bulb-Switcher-III/1375.py)