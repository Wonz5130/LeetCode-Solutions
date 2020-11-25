> LeetCode 0543. Diameter of Binary Tree二叉树的直径【Easy】【Python】【递归】

### Problem

[LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/)

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the **longest** path between any two nodes in a tree. This path may or may not pass through the root.

**Example:**
Given a binary tree

```
          1
         / \
        2   3
       / \     
      4   5    
```

Return **3**, which is the length of the path [4,2,1,3] or [5,2,1,3].

**Note:** The length of path between two nodes is represented by the number of edges between them.

### 问题

[力扣](https://leetcode-cn.com/problems/diameter-of-binary-tree/)

给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

**示例 :**
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 **3**, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

**注意：** 两结点之间的路径长度是以它们之间边的数目表示。

### 思路

**递归**

```
不是求左子树高度 + 右子树高度。
而是求任意两点之间的路径最大值。
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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max = 0
        self.depth(root)
        return self.max
    
    def depth(self, root):
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        # 更新最大值
        self.max = max(self.max, l + r)
        # 返回高度
        return max(l, r) + 1
```

### GitHub 地址

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0543-Diameter-of-Binary-Tree/0543.py)