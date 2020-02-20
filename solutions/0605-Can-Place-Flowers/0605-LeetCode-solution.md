> LeetCode 0605. Can Place Flowers种花问题【Easy】【Python】【贪心】

### Problem

[LeetCode](https://leetcode.com/problems/can-place-flowers/)

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number **n**, return if **n** new flowers can be planted in it without violating the no-adjacent-flowers rule.

**Example 1:**

```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
```

**Example 2:**

```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
```

**Note:**

1. The input array won't violate no-adjacent-flowers rule.
2. The input array size is in the range of [1, 20000].
3. **n** is a non-negative integer which won't exceed the input array size.

### 问题

[力扣](https://leetcode-cn.com/problems/can-place-flowers/)

假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 **n** 。能否在不打破种植规则的情况下种入 **n** 朵花？能则返回True，不能则返回False。

**示例 1:**

```
输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
```

**示例 2:**

```
输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
```

**注意:**

1. 数组内已种好的花不会违反种植规则。
2. 输入的数组长度范围为 [1, 20000]。
3. **n** 是非负整数，且不会超过输入数组的大小。

### 思路

**贪心**

从反面来看，不能种花的情况共有三种：

* 当前位置已有花
* 位置不是头，且左边已有花
* 位置不是尾，且右边已有花

其余情况可以种花。

**时间复杂度:** O(len(flowerbed))
**空间复杂度:** O(1)

### Python代码

```python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not flowerbed or len(flowerbed) == 0:
            return False
        cnt = 0
        for plot in range(len(flowerbed)):  # range:0 - len(flowerbed)-1
            if flowerbed[plot] == 1:  # already planted flower
                continue
            if plot > 0 and flowerbed[plot-1] == 1:  # left planted flower
                continue
            if plot < len(flowerbed) - 1 and flowerbed[plot + 1] == 1:  # right planted flower
                continue
            flowerbed[plot] = 1
            cnt += 1
        if cnt >= n:
            return True
        else:
            return False
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0605-Can-Place-Flowers/0605.py)