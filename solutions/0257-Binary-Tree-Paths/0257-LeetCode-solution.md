> LeetCode 0257. Binary Tree Paths二叉树的所有路径【Easy】【Python】【DFS】

### Problem

[LeetCode](https://leetcode.com/problems/binary-tree-paths/)

Given a binary tree, return all root-to-leaf paths.

**Note:** A leaf is a node with no children.

**Example:**

```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```

### 问题

[力扣](https://leetcode-cn.com/problems/binary-tree-paths/)

给定一个二叉树，返回所有从根节点到叶子节点的路径。

**说明:** 叶子节点是指没有子节点的节点。

**示例:**

```
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
```

### 思路

**DFS**

```
递归模板题。
先访问根节点，再判断分别左右子树。
如果是叶子节点，就保存到 ans 中，如果不是就加入到 path 中，继续访问直到到达叶子节点为止。
```

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        ans = []
        self.dfs(root, ans, '' + str(root.val))
        return ans

    def dfs(self, root, ans, path):
        if root.left == None and root.right == None:
            ans.append(path)
        if root.left != None:
            self.dfs(root.left, ans, path + '->' + str(root.left.val))
        if root.right != None:
            self.dfs(root.right, ans, path + '->' + str(root.right.val))
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0257-Binary-Tree-Paths/0257.py)