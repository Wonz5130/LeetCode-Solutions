> LeetCode 0530. Minimum Absolute Difference in BST二叉搜索树的最小绝对差【Easy】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

Given a binary search tree with non-negative values, find the minimum [absolute difference](https://en.wikipedia.org/wiki/Absolute_difference) between values of any two nodes.

**Example:**

```
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
```

**Note:**

- There are at least two nodes in this BST.
- This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

## 问题

[力扣](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/)

给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

**示例：**

```
输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
```

**提示：**

- 树中至少有 2 个节点。
- 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同

## 思路

**DFS**

```
法一：dfs遍历取节点值，再单独计算最小绝对差
法二：dfs遍历直接进行绝对值比较
```

### Python3 代码

**法一**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # solution one: dfs遍历取节点值，再单独计算最小绝对差
        def dfs(root):
            if not root:
                return
            # 中序遍历是递增的
            if root.left:
                dfs(root.left)
            tmp_val.append(root.val)
            if root.right:
                dfs(root.right)
        tmp_val = []
        dfs(root)
        res = float("inf")
        for i in range(len(tmp_val) - 1):
            res = min(res, abs(tmp_val[i] - tmp_val[i + 1]))
        return res
```

**法二**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # solution two: dfs遍历直接进行绝对值比较
        pre = -1
        res = float("inf")
        def dfs(root):
            nonlocal pre, res
            if not root:
                return
            # 中序遍历是递增的
            if root.left:
                dfs(root.left)
            if pre != -1:
                res = min(res, abs(pre - root.val))
            pre = root.val
            if root.right:
                dfs(root.right)
        dfs(root)
        return res
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/0530-Minimum-Absolute-Difference-in-BST)