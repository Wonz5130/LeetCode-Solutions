> LeetCode 面试题26. 树的子结构【Medium】【Python】【DFS】

### 问题

[力扣](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/)

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

```
   3
  / \
  4  5
 / \
 1  2
```

给定的树 B：

```
  4 
 /
1
```


返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

**示例 1：**

```
输入：A = [1,2,3], B = [3,1]
输出：false
```

**示例 2：**

```
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
```

**限制：**

`0 <= 节点个数 <= 10000`

### 思路

**两重DFS**

```
第一重：找到起点。先判断当前节点，如果不对就判断左子树和右子树。
第二重：从找到的起点开始判断剩下的点。
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
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        return self.dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
            
        
    def dfs(self, A: TreeNode, B:TreeNode):
        if not B:
            return True
        if not A:
            return False
        if not A.val == B.val:
            return False
        # A树的根与B树的根相等
        return self.dfs(A.left, B.left) and self.dfs(A.right, B.right)  # 注意这里是 and
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-26-shu-de-zi-jie-gou-lcof/26.py)

### 相似题目

[LeetCode 1367. 二叉树中的列表](https://leetcode-cn.com/problems/linked-list-in-binary-tree/)