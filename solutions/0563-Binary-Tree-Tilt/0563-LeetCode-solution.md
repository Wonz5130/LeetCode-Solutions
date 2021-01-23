> LeetCode 0563. Binary Tree Tilt二叉树的坡度【Easy】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/binary-tree-tilt/)

Given the `root` of a binary tree, return *the sum of every tree node's **tilt**.*

The **tilt** of a tree node is the **absolute difference** between the sum of all left subtree node **values** and all right subtree node **values**. If a node does not have a left child, then the sum of the left subtree node **values** is treated as `0`. The rule is similar if there the node does not have a right child.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/10/20/tilt1.jpg)

```
Input: root = [1,2,3]
Output: 1
Explanation: 
Tilt of node 2 : |0-0| = 0 (no children)
Tilt of node 3 : |0-0| = 0 (no children)
Tile of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
Sum of every tilt : 0 + 0 + 1 = 1
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/10/20/tilt2.jpg)

```
Input: root = [4,2,9,3,5,null,7]
Output: 15
Explanation: 
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 5 : |0-0| = 0 (no children)
Tilt of node 7 : |0-0| = 0 (no children)
Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15
```

**Example 3:**

![img](https://assets.leetcode.com/uploads/2020/10/20/tilt3.jpg)

```
Input: root = [21,7,14,1,1,2,2,3,3]
Output: 9
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 104]`.
- `-1000 <= Node.val <= 1000`

## 问题

[力扣](https://leetcode-cn.com/problems/binary-tree-tilt/)

给定一个二叉树，计算 **整个树** 的坡度 。

一个树的 **节点的坡度** 定义即为，该节点左子树的节点之和和右子树节点之和的 **差的绝对值** 。如果没有左子树的话，左子树的节点之和为 0 ；没有右子树的话也是一样。空结点的坡度是 0 。

**整个树** 的坡度就是其所有节点的坡度之和。

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/10/20/tilt1.jpg)

```
输入：root = [1,2,3]
输出：1
解释：
节点 2 的坡度：|0-0| = 0（没有子节点）
节点 3 的坡度：|0-0| = 0（没有子节点）
节点 1 的坡度：|2-3| = 1（左子树就是左子节点，所以和是 2 ；右子树就是右子节点，所以和是 3 ）
坡度总和：0 + 0 + 1 = 1
```

**示例 2：**

![img](https://assets.leetcode.com/uploads/2020/10/20/tilt2.jpg)

```
输入：root = [4,2,9,3,5,null,7]
输出：15
解释：
节点 3 的坡度：|0-0| = 0（没有子节点）
节点 5 的坡度：|0-0| = 0（没有子节点）
节点 7 的坡度：|0-0| = 0（没有子节点）
节点 2 的坡度：|3-5| = 2（左子树就是左子节点，所以和是 3 ；右子树就是右子节点，所以和是 5 ）
节点 9 的坡度：|0-7| = 7（没有左子树，所以和是 0 ；右子树正好是右子节点，所以和是 7 ）
节点 4 的坡度：|(3+5+2)-(9+7)| = |10-16| = 6（左子树值为 3、5 和 2 ，和是 10 ；右子树值为 9 和 7 ，和是 16 ）
坡度总和：0 + 0 + 0 + 2 + 7 + 6 = 15
```

**示例 3：**

![img](https://assets.leetcode.com/uploads/2020/10/20/tilt3.jpg)

```
输入：root = [21,7,14,1,1,2,2,3,3]
输出：9
```

**提示：**

- 树中节点数目的范围在 [0, 10^4] 内
- -1000 <= Node.val <= 1000

## 思路

**DFS**

```
后序遍历
每个节点要做的事：自己的值加上左右子树的坡度值。
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
    def findTilt(self, root: TreeNode) -> int:
        # 后序遍历
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            # if root.left:
            left = dfs(root.left)
            # if root.right:
            right = dfs(root.right)
            res += abs(left - right)
            return root.val + left + right
        
        res = 0
        dfs(root)
        return res
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0563-Binary-Tree-Tilt/0563.py)