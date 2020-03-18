> LeetCode 0105. Construct Binary Tree from Preorder and Inorder Traversal从前序与中序遍历序列构造二叉树【Medium】【Python】【二叉树】【递归】

### Problem

[LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

Given preorder and inorder traversal of a tree, construct the binary tree.

**Note:**
You may assume that duplicates do not exist in the tree.

For example, given

```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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

[力扣](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

根据一棵树的前序遍历与中序遍历构造二叉树。

**注意:**
你可以假设树中没有重复的元素。

例如，给出

```
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
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
前序遍历：根左右
中序遍历：左根右

于是，每次取前序遍历的值，表示根，再到中序遍历中确定索引。
再根据索引，分割成左子树和右子树。如此递归。

注意：
保证递归的 preorder 和 inorder 个数一致。
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])

        # 根在中序遍历中的索引
        i = inorder.index(root.val)
        # left: preorder[1] ~ preorder[i], inorder[0] ~ inorder[i-1]
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        # right: preorder[i+1] ~ preorder[-1], inorder[i+1] ~ inorder[-1]
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return root
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0105-Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal/0105.py)