> LeetCode 0652. Find Duplicate Subtrees 寻找重复的子树【Medium】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/find-duplicate-subtrees/)

给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

两棵树重复是指它们具有相同的结构以及相同的结点值。

**示例 1：**

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
下面是两个重复的子树：

      2
     /
    4
和

    4
因此，你需要以列表的形式返回上述重复子树的根结点。

## 思路

**后序遍历**

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
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        import collections
        res = []
        counter = collections.Counter()

        def traverse(root):
            if not root:
                return '#'
            # 后序遍历
            left = traverse(root.left)
            right = traverse(root.right)
            chain = left + ',' + right + ',' + str(root.val)
            counter[chain] += 1
            # 统计出现两次即是重复子树，加入res
            if counter[chain] == 2:
                res.append(root)
            return chain
        
        traverse(root)
        return res
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/0652-Find-Duplicate-Subtrees)