> LeetCode 0230. Kth Smallest Element in a BST二叉搜索树中第K小的元素【Medium】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

Given a binary search tree, write a function `kthSmallest` to find the **k**th smallest element in it.

**Example 1:**

```
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```

**Example 2:**

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```

**Follow up:**
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

**Constraints:**

- The number of elements of the BST is between `1` to `10^4`.
- You may assume `k` is always valid, `1 ≤ k ≤ BST's total elements`.

## 问题

[力扣](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/)

给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

**说明：**
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

**示例 1:**

```
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
```

**示例 2:**

```
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
```

**进阶：**
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？

## 思路

**中序遍历**

```
因为 BST 的中序遍历就是升序的，因此只需要中序遍历一下，然后取第 k 个元素就行。
```

### Python3 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 中序遍历
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        return inorder(root)[k - 1]
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0230-Kth-Smallest-Element-in-a-BST/0230.py)