> LeetCode 面试题 17.12. BiNode【Easy】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/binode-lcci/)

二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。

返回转换后的单向链表的头节点。

注意：本题相对原题稍作改动

**示例：**

```
输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
```

**提示：**

- 节点数量不会超过 100000。

## 思路

**DFS**

```
中序遍历
```

## 代码

### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            pre = cur = root
            if root:
                if root.left:
                    pre, cur = dfs(root.left)
                    # 左子树的下一个链表节点是当前root节点
                    cur.right = root
                    # 修改当前指针
                    cur = root
                    root.left = None
                if root.right:
                    root.right, cur = dfs(root.right)
            return pre, cur
        
        return dfs(root)[0]
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/Interview-17.12-BiNode-LCCI)