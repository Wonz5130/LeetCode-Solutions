> LeetCode 0034. Find First and Last Position of Element in Sorted Array在排序数组中查找元素的第一个和最后一个位置【Medium】【Python】【二分】

### Problem

[LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

Given an array of integers `nums` sorted in ascending order, find the starting and ending position of a given `target` value.

Your algorithm's runtime complexity must be in the order of *O*(log *n*).

If the target is not found in the array, return `[-1, -1]`.

**Example 1:**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

**Example 2:**

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

### 问题

[力扣](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

给定一个按照升序排列的整数数组 `nums`，和一个目标值 `target`。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 *O(log n)* 级别。

如果数组中不存在目标值，返回 `[-1, -1]`。

**示例 1:**

```
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
```

**示例 2:**

```
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
```

### 思路

**二分查找**

```
两次二分查找。
1. 查找 left，所以 nums[mid] < target 时，才移动 left 指针
2. 查找 right，所以 nums[mid] <= target 时，才移动 left 指针
3. lower_bound 返回的是开始的第一个满足条件的位置，而 upper_bound 返回的是第一个不满足条件的位置。所以，当两个相等的时候代表没有找到，如果找到了的话，需要返回的是 [left, right - 1]。
```

**时间复杂度:** O(logn)
**空间复杂度:** O(1)

### Python代码

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # solution one: binary search
        left = self.lowwer_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]
    
    def lowwer_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] < target:  # <
                left = mid + 1
            else:
                right = mid
        return left
    
    def higher_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] <= target:  # <=
                left = mid + 1
            else:
                right = mid
        return left

        # # solution two: bisect
        # left = bisect.bisect_left(nums, target)
        # right = bisect.bisect_right(nums, target)
        # if left == right:
        #     return [-1, -1]
        # return [left, right - 1]
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0034-Find-First-and-Last-Position-of-Element-in-Sorted-Array/0034.py)