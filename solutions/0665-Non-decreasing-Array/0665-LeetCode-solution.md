> LeetCode 0665. Non-decreasing Array非递减数列【Easy】【Python】【贪心】

### Problem

[LeetCode](https://leetcode.com/problems/non-decreasing-array/)

Given an array with `n` integers, your task is to check if it could become non-decreasing by modifying **at most** `1` element.

We define an array is non-decreasing if `array[i] <= array[i + 1]` holds for every `i` (1 <= i < n).

**Example 1:**

```
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
```

**Example 2:**

```
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
```

**Note:** The `n` belongs to [1, 10,000].

### 问题

[力扣](https://leetcode-cn.com/problems/non-decreasing-array/)

给定一个长度为 n 的整数数组，你的任务是判断在**最多**改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。

**示例 1:**

```
输入: [4,2,3]
输出: True
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
```

**示例 2:**

```
输入: [4,2,1]
输出: False
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
```


说明:  n 的范围为 [1, 10,000]。

### 思路

**贪心**

**法一**

用两个数组 nums1，nums2，分别复制 nums。当 nums[i] > nums[i+1] 时，nums1 变大，nums2 变小。仅进行一次改变就退出。然后比较 nums1 和排序之后的 nums1，以及比较 nums2 和排序之后的 nums2，只要有一个是相等的就返回 True。

**时间复杂度:** O(len(nums))
**空间复杂度:** O(len(nums))

**法二**

计数器 cnt 记录，遍历 nums，当 nums[i] > nums[i+1] 时，cnt 加一，然后分两种情况，一种是变得，一种是变小，详情可以看下面的代码注释。

**时间复杂度:** O(len(nums))
**空间复杂度:** O(1)

### Python代码

```python
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # # solution one
        # if len(nums) <= 2:
        #     return True
        # nums1, nums2= nums[:], nums[:]
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         nums1[i] = nums[i+1]  # change bigger
        #         nums2[i+1] = nums[i]  # change smaller
        #         break  # only change once, then break
        # return nums1 == sorted(nums1) or nums2 == sorted(nums2)

        # solution two
        if len(nums) <= 2:
            return True
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                cnt += 1
                if i == 1 or nums[i-2] <= nums[i]:  # 3,5,4 -> 3,4,4
                    nums[i-1] = nums[i]
                else:  # 4,5,4 -> 4,5,5
                    nums[i] = nums[i-1]
                if cnt > 1:
                    return False
        return True
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0665-Non-decreasing-Array/0665.py)