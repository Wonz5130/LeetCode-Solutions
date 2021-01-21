> LeetCode 0783. Minimum Distance Between BST Nodes二叉搜索树节点最小距离【Easy】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)

Given a Binary Search Tree (BST) with the root node `root`, return the minimum difference between the values of any two different nodes in the tree.

**Example :**

```
Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
```

**Note:**

1. The size of the BST will be between 2 and `100`.
2. The BST is always valid, each node's value is an integer, and each node's value is different.
3. This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/

## 问题

[力扣](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/)

给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。

**示例：**

```
输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树节点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \    
    1   3  

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
```

**注意：**

1. 二叉树的大小范围在 2 到 100。
2. 二叉树总是有效的，每个节点的值都是整数，且不重复。
3. 本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同

## 思路

**DFS**

```
法一：dfs遍历取节点值，再单独计算最小绝对差
法二：dfs遍历直接进行绝对值比较
```

### Python3 代码

**法一**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # solution one: dfs遍历取节点值，再单独计算最小绝对差
        def dfs(root):
            if not root:
                return
            # 中序遍历是递增的
            if root.left:
                dfs(root.left)
            tmp_val.append(root.val)
            if root.right:
                dfs(root.right)
        tmp_val = []
        dfs(root)
        res = float("inf")
        for i in range(len(tmp_val) - 1):
            res = min(res, abs(tmp_val[i] - tmp_val[i + 1]))
        return res
```

**法二**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # solution two: dfs遍历直接进行绝对值比较
        pre = -1
        res = float("inf")
        def dfs(root):
            nonlocal pre, res
            if not root:
                return
            # 中序遍历是递增的
            if root.left:
                dfs(root.left)
            if pre != -1:
                res = min(res, abs(pre - root.val))
            pre = root.val
            if root.right:
                dfs(root.right)
        dfs(root)
        return res
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0783-Minimum-Distance-Between-BST-Nodes/0783.py)