> LeetCode 面试题 04.04. 检查平衡性【Easy】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/check-balance-lcci/)

实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。

**示例 1:**

```
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
```

**示例 2:**

```
给定二叉树 [1,2,2,3,3,null,null,4,4]
      1
     / \
    2   2
   / \
  3   3
 / \
4   4
返回 false 。
```

## 思路

**递归**

```
不止根节点左右高度差小于等于1，左右子树也要满足平衡
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
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        # 计算树的高度
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        
        # 不止根节点左右高度差小于等于1，左右子树也要满足平衡
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/Interview-04.04-Check-Balance-LCCI)