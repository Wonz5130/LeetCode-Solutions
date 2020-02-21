> LeetCode 0053. Maximum Subarray最大子序和【Easy】【Python】【动态规划】

### Problem

[LeetCode](https://leetcode.com/problems/maximum-subarray/)

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Follow up:**

If you have figured out the O(*n*) solution, try coding another solution using the divide and conquer approach, which is more subtle.

### 问题

[力扣](https://leetcode-cn.com/problems/maximum-subarray/)

给定一个整数数组 `nums` ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**示例:**

```
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

**进阶:**

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

### 思路

**动态规划**

找到 dp 递推公式。dp 等于每个位置的数字加上前面的 dp，当前面的 dp 是负数时就不要加了。

**时间复杂度:** O(len(nums))
**空间复杂度:** O(1)

### Python代码

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = 0
        sum = -0xFFFFFFFF
        for i in range(len(nums)):
            dp = nums[i] + (dp if dp > 0 else 0)  # if dp > 0: dp = nums[i] + dp, else: dp = nums[i]
            sum = max(sum, dp)
        return sum
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0053-Maximum-Subarray/0053.py)