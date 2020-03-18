> LeetCode 0106. Construct Binary Tree from Inorder and Postorder Traversal从中序与后序遍历序列构造二叉树【Medium】【Python】【二叉树】【递归】

### Problem

[LeetCode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

Given inorder and postorder traversal of a tree, construct the binary tree.

**Note:**
You may assume that duplicates do not exist in the tree.

For example, given

```
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```

Return the following binary tree:

```
    3
   / \
  9  20
    /  \
   15   7
```

### 问题

[力扣](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

根据一棵树的中序遍历与后序遍历构造二叉树。

**注意:**
你可以假设树中没有重复的元素。

例如，给出

```
中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
```

返回如下的二叉树：

```
    3
   / \
  9  20
    /  \
   15   7
```

### 思路

**递归**

```
中序遍历：左根右
后序遍历：左右根

于是，每次取后序遍历末尾的值，表示根，再到中序遍历中确定索引。
再根据索引，分割成左子树和右子树。如此递归。

注意：
保证递归的 inorder 和 postorder 个数一致。
```

**时间复杂度:** O(n)，n 为节点个数。
**空间复杂度:** O(n)，n 为节点个数。

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])

        # 根在中序遍历中的索引
        i = inorder.index(root.val)
        # left: inorder[0] ~ inorder[i-1], postorder[0] ~ postorder[i-1]
        root.left = self.buildTree(inorder[:i], postorder[:i])
        # right: inorder[i+1] ~ inorder[-1], postorder[i] ~ postorder[-2]
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])

        return root
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0106-Construct-Binary-Tree-from-Inorder-and-Postorder-Traversal/0106.py)