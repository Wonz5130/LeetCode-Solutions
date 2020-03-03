> LeetCode 0088. Merge Sorted Array合并两个有序数组【Easy】【Python】【双指针】

### 题目

[LeetCode](https://leetcode.com/problems/merge-sorted-array/)

Given two sorted integer arrays *nums1* and *nums2*, merge *nums2* into *nums1* as one sorted array.

**Note:**

- The number of elements initialized in *nums1* and *nums2* are *m* and *n* respectively.
- You may assume that *nums1* has enough space (size that is greater or equal to *m* + *n*) to hold additional elements from *nums2*.

**Example:**

```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

### 翻译

[力扣](https://leetcode-cn.com/problems/merge-sorted-array/)

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

**说明:**

* 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。

* 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

  示例:

```
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
```

### 思路

**双指针**

逆序，nums1 从 第 m 元素往前，nums2 从第 n 元素往前，哪个大哪个存在 nums1 的第 n+m-1 位置，然后慢慢从后往前存。最后看一下 nums2 是否还有剩余，如果还有就全部加到 nums1 中。

**时间复杂度:** O(m+n)
**空间复杂度:** O(1)

##### Python3代码

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else: 
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:  # 如果 nums2 有剩余, 全部加到 nums1 中
            nums1[:n] = nums2[:n]
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0088-Merge-Sorted-Array/0088.py)

### 相关题目

[LeetCode 面试题 10.01. Sorted Merge LCCI](https://leetcode-cn.com/problems/sorted-merge-lcci/)

### 一点疑惑

如果 nums1 = [1,2,3,0,0,0,0]，而 nums2 = [2,5,6]，m = 3，n = 3，那么合并之后的 nums1 = [1,2,2,3,5,6,0]，多余的 0 并没有自动销掉。

