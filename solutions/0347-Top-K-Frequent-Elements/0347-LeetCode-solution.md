> LeetCode 0347. Top K Frequent Elements前 K 个高频元素【Medium】【Python】【桶排序】

### Problem

[LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)

Given a non-empty array of integers, return the ***k*** most frequent elements.

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

**Note:**

- You may assume *k* is always valid, 1 ≤ *k* ≤ number of unique elements.
- Your algorithm's time complexity **must be** better than O(*n* log *n*), where *n* is the array's size.

### 问题

[力扣](https://leetcode-cn.com/problems/top-k-frequent-elements/)

给定一个非空的整数数组，返回其中出现频率前 ***k*** 高的元素。

**示例 1:**

```
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
```

**示例 2:**

```
输入: nums = [1], k = 1
输出: [1]
```

**说明：**

- 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
- 你的算法的时间复杂度**必须**优于 O(*n log n*) , *n* 是数组的大小。

### 思路

**桶排序**

1. 先统计元素的频率，相同元素出现计数 + 1。
2. 再进行桶排序，按数组中的元素按照出现频率分组，即出现频率为 i 的元素存在第 i 个桶。
3. 最后，从桶中逆序取出前 k 个元素。

**时间复杂度**: O(n)
**空间复杂度**: O(n)

### Python代码

```python
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 统计元素的频率
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1  # 返回字典 count 中 num 元素对应的值, 没有就赋值为 0
        
        # 桶排序
        bucket = [[] for i in range(len(nums) + 1)]
        for key, value in count.items():
            bucket[value].append(key)
        
        # 逆序取出前 k 个元素
        res = list()
        for i in range(len(nums), -1, -1):  # 最后一个 -1 表示逆序
            if bucket[i]:
                res.extend(bucket[i])  # 在列表末尾追加元素
            if len(res) >= k:  # 只要前 k 个
                break
        return res[:k]  # 输出第 k 个之前的元素（包括第 k 个元素)
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0347-Top-K-Frequent-Elements/0347.py)