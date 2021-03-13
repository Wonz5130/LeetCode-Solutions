> LeetCode 面试题 04.05. 合法二叉搜索树【Medium】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/legal-binary-search-tree-lcci/)

实现一个函数，检查一棵二叉树是否为二叉搜索树。

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

## 思路

**递归**

```
二叉搜索树：根节点值大于左子树节点最大值，小于右子树节点最小值。
左右子树也要满足二叉搜索树性质。
```

## 代码

### Python3

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

    # 辅助函数
    def isValid(self, root: TreeNode, min_: TreeNode, max_: TreeNode):
        if not root:
            return True
        if min_ != None and root.val <= min_.val:
            return False
        if max_ != None and root.val >= max_.val:
            return False
        return self.isValid(root.left, min_, root) and self.isValid(root.right, root, max_)
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/Interview-04.05-Legal-Binary-Search-Tree-LCCI)