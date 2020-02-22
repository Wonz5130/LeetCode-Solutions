> LeetCode 0540. Single Element in a Sorted Array有序数组中的单一元素【Medium】【Python】【二分】

### Problem

[LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/)

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

**Example 1:**

```
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
```

**Example 2:**

```
Input: [3,3,7,7,10,11,11]
Output: 10
```

**Note:** Your solution should run in O(log n) time and O(1) space.

### 问题

[力扣](https://leetcode-cn.com/problems/single-element-in-a-sorted-array/)

给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

**示例 1:**

```
输入: [1,1,2,3,3,4,4,8,8]
输出: 2
```

**示例 2:**

```
输入: [3,3,7,7,10,11,11]
输出: 10
```

**注意:** 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。

### 思路

**解法一:**
**二分查找**

```
每次都取偶数位置的数，如果不是偶数位置，那 mid-1。
如果 nums[mid] != nums[mid + 1]，表示单个数在 mid 左边，否则在 mid 右边。
```

**时间复杂度:** O(logn)
**空间复杂度:** O(1)

**解法二:**
**判断相邻元素是否相等**

```
每隔两个位置遍历数组，如果 nums[i] != nums[i + 1]，那单个数就是 nums[i]，否则就是最后一个数。
```

**时间复杂度:** O(n/2)
**空间复杂度:** O(1)

### Python代码

```python
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution one: binary search
        low, high = 0, len(nums) - 1
        while low < high:
            mid = int((low + high) / 2)  # element in list must be int
            if mid % 2 == 1:  # even position
                mid -= 1
            if nums[mid] != nums[mid + 1]:  # result is on the left of mid
                high = mid
            else:
                low = mid + 2
        return nums[low]

        # # solution two: adjacent elements are equal
        # for i in range(0, len(nums) - 1, 2):  # step = 2
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        # return nums[-1]
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0540-Single-Element-in-a-Sorted-Array/0540.py)