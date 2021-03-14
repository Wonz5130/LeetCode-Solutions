> LeetCode 面试题 04.06. 后继者【Medium】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/successor-lcci/)

设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

如果指定节点没有对应的“下一个”节点，则返回null。

**示例 1:**

```
输入: root = [2,1,3], p = 1

  2
 / \
1   3

输出: 2
```

**示例 2:**

```
输入: root = [5,3,6,2,4,null,null,1], p = 6
      5
     / \
    3   6
   / \
  2   4
 /   
1

输出: null
```

## 思路

**递归**

```
p >= root：中序后继节点在右子树
p < root：左子树不为空就去左子树找，否则当前节点就是中序后继节点
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
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # p >= root，后继节点在右子树
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            # 左子树不为空
            if self.inorderSuccessor(root.left, p):
                return self.inorderSuccessor(root.left, p)
            # 左子树为空，当前节点就是后继节点
            else:
                return root
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/Interview-04.06-Successor-LCCI)