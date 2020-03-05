> LeetCode 0047. Permutations II全排列 II【Medium】【Python】【回溯】

### Problem

[LeetCode](https://leetcode.com/problems/permutations-ii/)

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

**Example:**

```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

### 问题

[力扣](https://leetcode-cn.com/problems/permutations-ii/)

给定一个可包含重复数字的序列，返回所有不重复的全排列。

**示例:**

```
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

### 思路

##### 解法一

**递归**

```
参考 LeetCode 0046，只需要加上判断 path 不重复就行。
即：path not in res。
```

##### Python3代码

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # solution one: recursion
        res = []
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, path):
        if not nums and path not in res:  # path should be unique
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])
```

##### 解法二

**回溯**

```
回溯三步骤：
1.有效结果：sol 长度等于 nums 长度。
2.回溯范围及答案更新。
3.剪枝条件：
	a.使用过的不能再使用，要剪枝。
	b.当前元素和前一个元素相同，并且前一个元素没有使用过，也要剪枝。
```

##### Python3代码

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # solution two: backtracking
        nums.sort()  # sort at first
        self.res = []
        check = [0 for _ in range(len(nums))]

        self.dfs([], nums, check)
        return self.res
    
    def dfs(self, sol, nums, check):
        # 1.valid result
        if len(sol) == len(nums):
            self.res.append(sol)
            return
        
        for i in range(len(nums)):
            # 3.pruning
            if check[i] == 1:  # used
                continue
            if i > 0 and nums[i] == nums[i - 1] and not check[i - 1]:
                continue

            # 2.backtrack and update check
            check[i] = 1
            self.dfs(sol + [nums[i]], nums, check)
            check[i] = 0  # after backtracking, should update check[i]
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0047-Permutations-II/0047.py)

### 参考

[sammy 题解](https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/)