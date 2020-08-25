> LeetCode 0491. Increasing Subsequences递增子序列【Medium】【Python】【DFS】

### Problem

[LeetCode](https://leetcode.com/problems/increasing-subsequences/)

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

**Example:**

```
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
```

**Constraints:**

- The length of the given array will not exceed 15.
- The range of integer in the given array is [-100,100].
- The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

### 问题

[力扣](https://leetcode-cn.com/problems/increasing-subsequences/)

给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

**示例:**

```
输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
```

**说明:**

1. 给定数组的长度不会超过15。
2. 数组中的整数范围是 [-100,100]。
3. 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

### 思路

**DFS**

##### Python3代码

```python
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    	# solution one：DFS
    	res = []

    	def dfs(nums, tmp):
    		if len(tmp) > 1:
    			res.append(tmp)

    		cur_pres = set()
    		# 循环 nums 的索引值对
    		for inx, i in enumerate(nums):
    			# 当前值已经被遍历
    			if i in cur_pres:
    				continue
    			# 当前值可以加入组成递增子序列
    			if not tmp or i >= tmp[-1]:
    				cur_pres.add(i)
    				dfs(nums[inx + 1:], tmp + [i])

    	dfs(nums, [])
    	return res
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0491-Increasing-Subsequences/0491.py)