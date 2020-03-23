> LeetCode 面试题 04.10. 检查子树【Medium】【Python】【DFS】

### 问题

[力扣](https://leetcode-cn.com/problems/check-subtree-lcci/)

检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。

如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

**示例1:**

```
 输入：t1 = [1, 2, 3], t2 = [2]
 输出：true
```

**示例2:**

```
 输入：t1 = [1, null, 2, 4], t2 = [3, 2]
 输出：false
```

**提示：**

1. 树的节点数目范围为[0, 20000]。

### 思路

**两重DFS**

```
第一重：在 t1 中找到 t2 的起点。先判断 t1 当前节点，如果不对就判断 t1 左子树和 t1 右子树。
第二重：从找到的起点开始判断剩下的点，t1 和 t2 同步左右子树搜索。
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
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None:
            return False
        if t2 == None:
            return True
        # find the root of t2 in t1
        return self.dfs(t1, t2) or self.checkSubTree(t1.left , t2) or self.checkSubTree(t1.right, t2)
    
    def dfs(self, t1, t2):
        # t2 is over
        if t2 == None:
            return True
        # t2 is not over and t1 is over
        elif t2 != None and t1 == None:
            return False
        # not equal
        elif t2.val != t1.val:
            return False
        # equal, then search left and right
        else:
            return self.dfs(t1.left, t2.left) and self.dfs(t1.right, t2.right)  # 注意这里是and
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-04.10-check-subtree-lcci/0410.py)

### 相关题目

[LeetCode 1367. Linked List in Binary Tree二叉树中的列表](https://leetcode-cn.com/problems/linked-list-in-binary-tree/)