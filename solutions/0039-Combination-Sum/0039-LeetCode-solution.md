> LeetCode 0039. Combination Sum组合总和【Medium】【Python】【回溯】

### Problem

[LeetCode](https://leetcode.com/problems/combination-sum/description/)

Given a **set** of candidate numbers (`candidates`) **(without duplicates)** and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

The **same** repeated number may be chosen from `candidates` unlimited number of times.

**Note:**

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

**Example 2:**

```
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

### 问题

[力扣](https://leetcode-cn.com/problems/combination-sum/)

给定一个**无重复元素**的数组 `candidates` 和一个目标数 `target` ，找出 `candidates` 中所有可以使数字和为 `target` 的组合。

`candidates` 中的数字可以无限制重复被选取。

说明：

* 所有数字（包括 `target`）都是正整数。
* 解集不能包含重复的组合。 

**示例 1:**

```
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
```

**示例 2:**

```
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
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

作者：jeromememory
链接：https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-tao-mo-ban-ji-ke-by-jeromememory/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

##### Python3代码

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
            # 2.backtrack and update 回溯以及更新 path
            path.append(candidates[i])
            self.dfs(candidates, i, n, path, res, tmp)
            path.pop()
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0039-Combination-Sum/0039.py)

### 参考

[回溯算法 + 剪枝](https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/)