> LeetCode 0215. Kth Largest Element in an Array数组中的第K个最大元素【Medium】【Python】【快排】【堆】

### Problem

[LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)

Find the **k**th largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

**Example 1:**

```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

**Example 2:**

```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```

**Note:**
You may assume k is always valid, 1 ≤ k ≤ array's length.

### 问题

[力扣](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

在未排序的数组中找到第 **k** 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

**示例 1:**

```
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
```

**示例 2:**

```
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
```

**说明:**

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

### 思路

**法一：快排**

找出第 **k** 个最大的元素，可以看成将数组从大到小排序，取第 **k** 个位置的元素。选择使用快排，即当分界点的索引是 k-1 时，就是第 **k** 个最大元素。详情可以参考[耶鲁大学关于QuickSelect算法的介绍](http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html)。

**时间复杂度**: O(n)
**空间复杂度**: O(1)

**法二：堆**

构建最大堆，从上往下，第 **k** 个位置就是第 **k** 个最大元素。

**时间复杂度**: O(nlogk)
**空间复杂度**: O(k)

### Python代码

```python
# 法一：快排
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while low <= high:
            pivot = self.partition(nums, low, high)
            if pivot == k - 1:  # 第 k 大, 即从大到小排序第 k-1 位置(从 0 开始计算)
                return nums[pivot]
            if pivot < k - 1:
                low = pivot + 1
            else:
                high = pivot - 1
    
    # 划分函数
    def partition(self, nums, low, high):
        pivot_value = nums[high]  # 因为是从大到小排序, 所以选 nums[high] 为基值
        index = low
        for i in range(low, high):
            if nums[i] >= pivot_value:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        nums[index], nums[high] = nums[high], nums[index]
        return index  # 返回的 index 即分界点

# 法二：堆
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 直接调用 Python 的 heapq 模块
        import heapq
        list_k = heapq.nlargest(k, nums)
        return list_k.pop()
```

### 题外话

其实用 Python 自带的 sorted() 函数排序也能 AC。

```Python
return sorted(nums)[-k]  # 用 Python 自带的排序算法一行代码就能 AC
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0215-Kth-Largest-Element-in-an-Array/0215.py)