> LeetCode 0671. Second Minimum Node In a Binary Tree 二叉树中第二小的节点【Easy】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/)

给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/smbt1.jpg)

```
输入：root = [2,2,5,null,null,5,7]
输出：5
解释：最小的值是 2 ，第二小的值是 5 。
```

**示例 2：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/smbt2.jpg)

```
输入：root = [2,2,2]
输出：-1
解释：最小的值是 2, 但是不存在第二小的值。
```

**提示：**

- 树中节点数目在范围 [1, 25] 内
- 1 <= Node.val <= 231 - 1
- 对于树中每个节点 root.val == min(root.left.val, root.right.val)

## 思路

**DFS**

```
根据题意，最小元素一定是根节点，所以只要找到比根节点大的节点就行。
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
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        def dfs(root, val):
            if not root:
                return -1
            # 根据题意，最小元素一定是根节点，所以只要找到比根节点大的节点就行
            if root.val > val:
                return root.val
            left = dfs(root.left, val)
            right = dfs(root.right, val)
            if left == -1:
                return right
            if right == -1:
                return left
            return min(left, right)
        
        return dfs(root, root.val)
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/0671-Second-Minimum-Node-In-a-Binary-Tree)