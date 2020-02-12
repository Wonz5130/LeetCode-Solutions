> LeetCode 0167: Two Sum II - Input array is sorted【Python】

### 题目

[英文题目链接](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

Given an array of integers that is already ***sorted in ascending order\***, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

**Note:**

- Your returned answers (both index1 and index2) are not zero-based.
- You may assume that each input would have *exactly* one solution and you may not use the *same* element twice.

**Example:**

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

### 翻译

[中文题目链接](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

**说明:**

- 返回的下标值（index1 和 index2）不是从零开始的。

- 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

**示例:**

```
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
```

### 思路

**双指针**

left 指针从头指向尾，right 指针从尾指向头，然后判断两数之和是否等于 target。

**时间复杂度**：O(n)

### 代码

```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0  # 从头指向尾
        right = len(numbers) - 1  # 从尾指向头
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1 
            else:
                left += 1 
        return []
```

### 本地测试版本代码

```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0  # 从头指向尾
        right = len(numbers) - 1  # 从尾指向头
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1 
            else:
                left += 1 
        return []

if __name__ == "__main__":
    array = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(array, target))
```

