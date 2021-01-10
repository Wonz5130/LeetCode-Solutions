> LeetCode 0144. Binary Tree Preorder Traversal二叉树的前序遍历【Medium】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/binary-tree-preorder-traversal/)

Given the `root` of a binary tree, return *the preorder traversal of its nodes' values*.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```
Input: root = [1,null,2,3]
Output: [1,2,3]
```

**Example 2:**

```
Input: root = []
Output: []
```

**Example 3:**

```
Input: root = [1]
Output: [1]
```

**Example 4:**

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg)

```
Input: root = [1,2]
Output: [1,2]
```

**Example 5:**

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg)

```
Input: root = [1,null,2]
Output: [1,2]
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up:**

Recursive solution is trivial, could you do it iteratively?

## 问题

[力扣](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)

给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```
输入：root = [1,null,2,3]
输出：[1,2,3]
```

**示例 2：**

```
输入：root = []
输出：[]
```

**示例 3：**

```
输入：root = [1]
输出：[1]
```

**示例 4：**

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg)

```
输入：root = [1,2]
输出：[1,2]
```

**示例 5：**

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg)

```
输入：root = [1,null,2]
输出：[1,2]
```

**提示：**

- 树中节点数目在范围 [0, 100] 内
- -100 <= Node.val <= 100


进阶：递归算法很简单，你可以通过迭代算法完成吗？

## 思路

**递归**

```
根左右
先加入 root 节点的值，再遍历左右子树
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        res = []
        def dfs(root):
            if not root:
                return []
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return res
```

**迭代**

```
使用栈来模拟
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 迭代
        res = []
        if not root:
            return res
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                # 前序遍历
                node = node.left
            node = stack.pop()
            node = node.right
        return res
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0144-Binary-Tree-Preorder-Traversal/0144.py)