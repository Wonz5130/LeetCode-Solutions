> LeetCode 0226. Invert Binary Tree翻转二叉树【Easy】【Python】【二叉树】【递归】

### Problem

[LeetCode](https://leetcode.com/problems/invert-binary-tree/)

Invert a binary tree.

**Example:**

Input:

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```

Output:

```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

**Trivia:**
This problem was inspired by [this original tweet](https://twitter.com/mxcl/status/608682016205344768) by [Max Howell](https://twitter.com/mxcl):

> Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

### 问题

[力扣](https://leetcode-cn.com/problems/invert-binary-tree/)

翻转一棵二叉树。

**示例：**

输入：

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```

输出：

```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

**备注:**
这个问题是受到 [Max Howell ](https://twitter.com/mxcl)的 [原问题](https://twitter.com/mxcl/status/608682016205344768) 启发的 ：

> 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

### 思路

##### 解法一

**递归**

```
前序遍历二叉树，如果当前节点有子树，就交换左右子树。
```

##### Python3 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # solution one: 递归
        if not root:
            return None
        # 叶子节点，直接返回自己
        if not root.left and not root.right:
            return root
        
        # 交换非叶子节点的左右两棵子树
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root
```

##### Go 代码

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
	// 前序遍历
	if root == nil {
		return nil
	}
	
	root.Left, root.Right = root.Right, root.Left

	invertTree(root.Left)
	invertTree(root.Right)

	return root
}

func invertTree(root *TreeNode) *TreeNode {
	// 后序遍历
	if root == nil {
		return nil
	}

	invertTree(root.Left)
	invertTree(root.Right)

	root.Left, root.Right = root.Right, root.Left

	return root
}
```

##### 解法二

**栈**

```
用栈模拟二叉树。
```

##### Python3 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # solution two: 栈
        if not root:
            return None
        # 叶子节点，直接返回自己
        if not root.left and not root.right:
            return root
        
        # 栈模拟二叉树
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.right)
                stack.append(node.left)
        return root
```

### GitHub 链接

- [Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0226-Invert-Binary-Tree/0226.py)

- [Go](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0226-Invert-Binary-Tree/0226.go)