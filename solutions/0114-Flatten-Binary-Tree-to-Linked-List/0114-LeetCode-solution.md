> LeetCode 0114. Flatten Binary Tree to Linked List二叉树展开为链表【Medium】【Python】【Go】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

```
    1
   / \
  2   5
 / \   \
3   4   6
```

The flattened tree should look like:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

## 问题

[力扣](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/)

给定一个二叉树，原地将它展开为一个单链表。

例如，给定二叉树

    	1
       / \
      2   5
     / \   \
    3   4   6

将其展开为：

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

## 思路

**递归**

```
1. 先将左右子树拉平成链表
2. 再把左子树作为新的右子树
3. 最后把原先右子树接到当前右子树末端
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # 递归调用
        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历：左-右-根
        # 左右子树拉平成链表
        left = TreeNode()
        left = root.left
        right = TreeNode()
        right = root.right

        # 左子树作为右子树
        root.left = None
        root.right = left

        # 原先右子树接到当前右子树末端
        p = TreeNode()
        p = root
        # 找到当前右子树末端
        while p.right != None:
            p = p.right
        p.right = right
```

### Go 代码

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func flatten(root *TreeNode) {
	if root == nil {
		return
	}
	// 递归调用
	flatten(root.Left)
	flatten(root.Right)

	// 后序遍历：左-右-根
	// 左右子树拉平成链表
	var left = new(TreeNode)
	left = root.Left
	var right = new(TreeNode)
	right = root.Right

	// 左子树作为右子树
	root.Left = nil
	root.Right = left

	// 原先右子树接到当前右子树末端
	var p = new(TreeNode)
	p = root
	// 找到当前右子树末端
	for {
		if p.Right == nil {
			break
		}
		p = p.Right
	} 
	p.Right = right
}
```

## GitHub 链接

- [Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0114-Flatten-Binary-Tree-to-Linked-List/0114.py)

- [Go](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0114-Flatten-Binary-Tree-to-Linked-List/0114.go)