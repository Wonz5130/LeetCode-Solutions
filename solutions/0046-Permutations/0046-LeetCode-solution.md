> LeetCode 0046. Permutations全排列【Medium】【Python】【回溯】【DFS】

### Problem

Given a collection of **distinct** integers, return all possible permutations.

**Example:**

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

### 问题

[力扣](https://leetcode-cn.com/problems/permutations/)

给定一个没有重复数字的序列，返回其所有可能的全排列。

**示例:**

```
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

### 思路

##### 解法一

**permutations函数**

##### Python3代码

```python
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # solution one: permutations
        return list(permutations(nums))
```

##### 解法二

**递归**

```
已有的排列放入 path 中，当 nums 为空表示递归完成，再把 path 放入 res 中。
```

##### Python3代码

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # solution two: recursion
        res = []
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])
```

##### 解法三

**回溯**

```
visited 数组表示是否访问过这个位置。
```

##### Python3代码

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # solution three: backtracking
        visited = [0] * len(nums)
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0
        
        dfs([])
        return res
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0046-Permutations/0046.py)