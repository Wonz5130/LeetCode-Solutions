> LeetCode 0153. Find Minimum in Rotated Sorted Array寻找旋转排序数组中的最小值【Medium】【Python】【二分】

### Problem

[LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).

Find the minimum element.

You may assume no duplicate exists in the array.

**Example 1:**

```
Input: [3,4,5,1,2] 
Output: 1
```

**Example 2:**

```
Input: [4,5,6,7,0,1,2]
Output: 0
```

### 问题

[力扣](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 `[0,1,2,4,5,6,7]` 可能变为 `[4,5,6,7,0,1,2]` )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

**示例 1:**

```
输入: [3,4,5,1,2]
输出: 1
```

**示例 2:**

```
输入: [4,5,6,7,0,1,2]
输出: 0
```

### 思路

**二分查找**

```
看到有序的数组就想到二分查找。
nums[mid] <= nums[high]: 表示在 mid 左侧
nums[mid] > nums[high]: 表示在 mid 右侧
```

**时间复杂度:** O(logn)
**空间复杂度:** O(1)

### Python代码

```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:  # < not <=, or <= will TLE
            mid = int((low + high) / 2)
            if nums[mid] <= nums[high]:  # <=
                high = mid  # h = m not m - 1
            else:
                low = mid + 1
        return nums[low]
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0153-Find-Minimum-in-Rotated-Sorted-Array/0153.py)