> LeetCode 0090. Subsets II子集II【Medium】【Python】【回溯】

### Problem

[LeetCode](https://leetcode.com/problems/subsets-ii/)

Given a collection of integers that might contain duplicates, **nums**, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**

```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

### 问题

[力扣](https://leetcode-cn.com/problems/subsets-ii/)

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

**说明：** 解集不能包含重复的子集。

**示例:**

```
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

### 思路

**回溯**

```
在 LeetCode 0070 题基础上，判断当前元素是否和前一个元素相同，相同就剪枝。
```

##### Python3 代码

```python
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        # 先对 nums 进行排序
        nums.sort()

        def backtrack(nums, start, path):
            # 加入 res
            res.append(path)
            # i 从 start 开始递增
            for i in range(start, n):
                # 剪枝：当前元素和前一个元素相同
                if i > start and nums[i - 1] == nums[i]:
                    continue
                # 回溯及更新 path
                # path.append([nums[i]])
                backtrack(nums, i + 1, path + [nums[i]])
                # path.pop()
        
        backtrack(nums, 0, [])
        return res
```

### GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0090-Subsets-II/0090.py)