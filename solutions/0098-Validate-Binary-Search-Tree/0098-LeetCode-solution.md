> LeetCode 0098. Validate Binary Search Tree验证二叉搜索树【Medium】【Python】【二叉树】

### Problem

[LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**

```
    2
   / \
  1   3

Input: [2,1,3]
Output: true
```

**Example 2:**

```
    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

### 问题

[力扣](https://leetcode-cn.com/problems/validate-binary-search-tree/)

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

* 节点的左子树只包含小于当前节点的数。
* 节点的右子树只包含大于当前节点的数。
* 所有左子树和右子树自身必须也是二叉搜索树。

**示例 1:**

```
输入:
    2
   / \
  1   3
输出: true
```

**示例 2:**

```
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
```

### 思路

**二叉树**

```
root 不只需要和左右子节点比较，而是和整个左右子树所有节点比较。
```

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, None, None)
    
    def isValid(self, root: TreeNode, min_: TreeNode, max_: TreeNode):
        if not root:
            return True
        if min_ != None and root.val <= min_.val:
            return False
        if max_ != None and root.val >= max_.val:
            return False
        return self.isValid(root.left, min_, root) and self.isValid(root.right, root, max_)
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0098-Validate-Binary-Search-Tree/0098.py)