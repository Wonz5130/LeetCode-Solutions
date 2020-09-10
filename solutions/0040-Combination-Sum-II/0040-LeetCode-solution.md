> LeetCode 0040. Combination Sum II组合总和 II【Medium】【Python】【回溯】

### Problem

[LeetCode](https://leetcode.com/problems/combination-sum-ii/)

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:**

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

**Example 2:**

```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

### 问题

[力扣](https://leetcode-cn.com/problems/combination-sum-ii/)

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

**说明：**

- 所有数字（包括目标数）都是正整数。
- 解集不能包含重复的组合。 

**示例 1:**

```txt
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

**示例 2:**

```txt
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
```

### 思路

**回溯模板**

```python
res = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        res.append(路径)
        return

for 选择 in 选择列表:
    做选择
    backtrack(路径, 选择列表)
    撤销选择
```

##### Python3 代码

```python
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        if n == 0:
            return []
        
        # accelerate 剪枝提速，非必需
        candidates.sort()

        path, res = [], []
        self.dfs(candidates, 0, n, path, res, target)
        return res
    
    def dfs(self, candidates, start, n, path, res, target):
        # 1.valid result 递归终止情况
        if target == 0:
            res.append(path[:])
            return
        
        for i in range(start, n):
            tmp = target - candidates[i]
            # 3.pruning 剪枝
            if tmp < 0:
                break
            # 防止出现这种情况：一个数字使用多次
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # 2.backtrack and update 回溯以及更新 path
            path.append(candidates[i])
            self.dfs(candidates, i + 1, n, path, res, tmp)
            path.pop()
```

### GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0040-Combination-Sum-II/0040.py)