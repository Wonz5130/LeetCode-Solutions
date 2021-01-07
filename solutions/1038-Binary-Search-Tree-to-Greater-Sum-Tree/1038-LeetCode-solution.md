> LeetCode 1038. 把二叉搜索树转换为累加树Binary Search Tree to Greater Sum Tree【Medium】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)

Given the `root` of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a *binary search tree* is a tree that satisfies these constraints:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Note:** This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/

**Example 1:**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/tree.png)

```
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
```

**Example 2:**

```
Input: root = [0,null,1]
Output: [1,null,1]
```

**Example 3:**

```
Input: root = [1,0,2]
Output: [3,3,2]
```

**Example 4:**

```
Input: root = [3,2,4,1]
Output: [7,9,4,10]
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 100]`.
- `0 <= Node.val <= 100`
- All the values in the tree are **unique**.
- `root` is guaranteed to be a valid binary search tree.

## 问题

[力扣](https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/)

给出二叉 **搜索** 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

- 节点的左子树仅包含键 **小于** 节点键的节点。
- 节点的右子树仅包含键 **大于** 节点键的节点。
- 左右子树也必须是二叉搜索树。

**注意：**该题目与 538: [https://leetcode-cn.com/problems/convert-bst-to-greater-tree/ ](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/)相同

**示例 1：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/tree.png)

```
输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
```

**示例 2：**

```
输入：root = [0,null,1]
输出：[1,null,1]
```

**示例 3：**

```
输入：root = [1,0,2]
输出：[3,3,2]
```

**示例 4：**

```
输入：root = [3,2,4,1]
输出：[7,9,4,10]
```

**提示：**

- 树中的节点数介于 `1` 和 `100` 之间。
- 每个节点的值介于 `0` 和 `100` 之间。
- 树中的所有值 **互不相同** 。
- 给定的树为二叉搜索树。

## 思路

**中序遍历**

```
利用 BST 的中序遍历就是升序的特性，降序遍历 BST 的元素值。
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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            nonlocal sumval
            if root:
                dfs(root.right)
                sumval += root.val
                root.val = sumval  # 将BST转化成累加树
                dfs(root.left)
        
        sumval = 0
        dfs(root)
        return root
```

## GitHub 链接

[Python]()