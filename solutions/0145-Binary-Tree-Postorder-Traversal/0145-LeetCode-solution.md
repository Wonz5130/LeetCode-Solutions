> LeetCode 0145. Binary Tree Postorder Traversal二叉树的后序遍历【Medium】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/binary-tree-postorder-traversal/)

Given the `root` of a binary tree, return *the postorder traversal of its nodes' values*.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/08/28/pre1.jpg)

```
Input: root = [1,null,2,3]
Output: [3,2,1]
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

![img](https://assets.leetcode.com/uploads/2020/08/28/pre3.jpg)

```
Input: root = [1,2]
Output: [2,1]
```

**Example 5:**

![img](https://assets.leetcode.com/uploads/2020/08/28/pre2.jpg)

```
Input: root = [1,null,2]
Output: [2,1]
```

**Constraints:**

- The number of the nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up:**

Recursive solution is trivial, could you do it iteratively?

## 问题

[力扣](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)

给定一个二叉树，返回它的 后序 遍历。

**示例:**

```
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
```

**进阶:** 递归算法很简单，你可以通过迭代算法完成吗？

## 思路

**递归**

```
左右根
先遍历左右子树，再加入 root 节点的值。
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        res = []
        def dfs(root):
            if not root:
                return []
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 迭代
        res = []
        if not root:
            return res
        stack = []
        node = root
        while stack or node:
            while node:
                # 根节点入栈
                stack.append(node)
                # 左子树存在
                if node.left:
                    node = node.left
                # 左子树不存在，转右子树
                else:
                    node = node.right
            # 取出栈顶元素
            node = stack.pop()
            res.append(node.val)
            # 栈不为空且当前节点是栈顶元素的左节点
            # stack[-1]就是取出的栈顶元素：node
            if stack and node == stack[-1].left:
                node = stack[-1].right
            # 没有左子树或右子树，退栈
            else:
                node = None
        return res
```

## GitHub 链接

[Python]()