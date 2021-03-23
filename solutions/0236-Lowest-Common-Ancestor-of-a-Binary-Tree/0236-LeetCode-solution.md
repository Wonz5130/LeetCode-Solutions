> LeetCode 0236. Lowest Common Ancestor of a Binary Tree 二叉树的最近公共祖先【Medium】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

**示例 1：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/binarytree.png)

```
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
```

**示例 2：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/binarytree.png)

```
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
```

**示例 3：**

```
输入：root = [1,2], p = 1, q = 2
输出：1
```

**提示：**

- 树中节点数目在范围 [2, 105] 内。
- -109 <= Node.val <= 109
- 所有 Node.val 互不相同 。
- p != q
- p 和 q 均存在于给定的二叉树中。

## 思路

**DFS**

```
后序遍历分四种情况：
1. 左右子树都为空：左右子树都不包含p，q
2. 左子树为空：p，q 都不在左子树中
3. 右子树为空：p，q 都不在右子树中
4. 左右子树都不为空：p，q 分别在左右子树，当前 root 就是最近公共祖先节点
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 左右子树都为空
        if not left and not right:
            return None
        # 右子树为空
        elif left and not right:
            return left
        # 左子树为空
        elif not left and right:
            return right
        # 左右子树都不为空
        return root
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/0236-Lowest-Common-Ancestor-of-a-Binary-Tree)
