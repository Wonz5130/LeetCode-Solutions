> LeetCode 0100. Same Tree 相同的树【Easy】【Python】【二叉树】

### Problem

[LeetCode](https://leetcode.com/problems/same-tree/)

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

**Example 1:**

```
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
```

**Example 2:**

```
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
```

**Example 3:**

```
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
```

### 问题

[力扣](https://leetcode-cn.com/problems/same-tree/)

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

**示例 1:**

```
输入:       1         1
          / \       / \
         2   3     2   3
        [1,2,3],   [1,2,3]
输出: true
```

**示例 2:**

```
输入:      1          1
          /           \
         2             2
        [1,2],     [1,null,2]
输出: false
```

**示例 3:**

```
输入:       1         1
          / \       / \
         2   1     1   2
        [1,2,1],   [1,1,2]
输出: false
```

### 思路

**二叉树**

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 两棵树都为空
        if not p and not q:
            return True
        # 一棵树为空，另一棵不为空
        elif not p or not q:
            return False
        # 两棵树都非空，但节点值不同
        elif p.val != q.val:
            return False
        # 分别判断左子树和右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0100-Same-Tree/0100.py)