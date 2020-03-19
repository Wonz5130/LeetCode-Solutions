> LeetCode 面试题27. 二叉树的镜像【剑指Offer】【Easy】【Python】【二叉树】【递归】

### 问题

[力扣](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/)

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```

镜像输出：

```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

**示例 1：**

```
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
```

**限制：**

```
0 <= 节点个数 <= 1000
```

注意：本题与主站 [226 题](https://leetcode-cn.com/problems/invert-binary-tree/) 相同

### 思路

**递归**

```
前序遍历二叉树，如果当前节点有子树，就交换左右子树。
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
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        # 叶子节点，直接返回自己
        if not root.left and not root.right:
            return root
        
        # 交换非叶子节点的左右两棵子树
        root.left, root.right = root.right, root.left
        if root.left:
            self.mirrorTree(root.left)
        if root.right:
            self.mirrorTree(root.right)
        return root
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-27-er-cha-shu-de-jing-xiang-lcof/27.py)