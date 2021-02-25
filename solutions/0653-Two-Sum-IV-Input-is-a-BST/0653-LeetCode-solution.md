> LeetCode 0653. Two Sum IV - Input is a BST 两数之和 IV - 输入 BST【Easy】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/)

给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

**案例 1:**

```
输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
```

**案例 2:**

```
输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False
```

## 思路

**中序遍历**

```
利用二叉搜索树中序遍历是递增序列的特性，再利用双指针找出两数之和等于目标值。
```

## 代码

### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # 中序遍历是递增序列
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        val = inorder(root)
        # 双指针
        left, right = 0, len(val) - 1
        while left < right:
            sumVal = val[left] + val[right]
            if sumVal == k:
                return True
            elif sumVal > k:
                right -= 1
            else:
                left += 1
        return False
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/0653-Two-Sum-IV-Input-is-a-BST)