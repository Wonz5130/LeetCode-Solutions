> LeetCode 0075. Sort Colors颜色分类【Medium】【Python】【荷兰旗】

### Problem

[LeetCode](https://leetcode.com/problems/sort-colors/)

Given an array with n objects colored red, white or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

**Note:** You are not suppose to use the library's sort function for this problem.

**Example:**

```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Follow up:**

* A rather straight forward solution is a two-pass algorithm using counting sort.
  First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
* Could you come up with a one-pass algorithm using only constant space?

### 问题

[力扣](https://leetcode-cn.com/problems/sort-colors/)

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

**注意:** 不能使用代码库中的排序函数来解决这道题。

**示例:**

```
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
```

**进阶：**

* 一个直观的解决方案是使用计数排序的两趟扫描算法。
  首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
* 你能想出一个仅使用常数空间的一趟扫描算法吗？

### 思路

**荷兰旗**

三个指针，left，mid，right，其中 mid 指针用来遍历数组。

* mid 指向 0，交换 left 与 mid， left++，mid++
* mid 指向 1，不做任何交换，mid++
* mid 指向 2，交换 right 与 mid，right--

mid 指向 2 的时候，只需要 right-- 就行，而不需要 mid++，因为如果交换过来的是 0，需要做进一步处理。

关于荷兰旗问题，详情请参考[Wiki](https://en.wikipedia.org/wiki/Dutch_national_flag_problem)。

也可以直接用分类做，分成 red，white，blue 三类。

**时间复杂度**: O(n)
**空间复杂度**: O(1)

### Python代码

```python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # # 法一：分类
        # red, white, blue = 0, 0, 0
        # for i in nums:
        #     if i == 0:
        #         red += 1
        #     elif i == 1:
        #         white += 1
        # for i in range(red):
        #     nums[i] = 0
        # for i in range(red, red+white):
        #     nums[i] = 1
        # for i in range(red+white, len(nums)):
        #     nums[i] = 2
        
        # 法二：荷兰旗问题 三指针
        left, mid, right = 0, 0, len(nums)-1
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1  # 只需要right往左移一位就行，mid不需要动
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0075-Sort-Colors/0075.py)