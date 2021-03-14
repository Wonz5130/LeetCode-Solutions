> LeetCode 面试题 04.08. 首个共同祖先【Medium】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/first-common-ancestor-lcci/)

设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。

例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]

    	3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
**示例 1:**

```
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
```

**示例 2:**

```
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
```

**说明:**

```
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
```

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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
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
        else:
            return root
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/Interview-04.08-First-Common-Ancestor-LCCI)