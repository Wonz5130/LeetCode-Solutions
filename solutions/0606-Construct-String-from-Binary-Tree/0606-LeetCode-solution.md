> LeetCode 0606. Construct String from Binary Tree 根据二叉树创建字符串【Easy】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/construct-string-from-binary-tree/)

你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

**示例 1:**

```
输入: 二叉树: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

输出: "1(2(4))(3)"

解释: 原本将是“1(2(4)())(3())”，
在你省略所有不必要的空括号对之后，
它将是“1(2(4))(3)”。
```

**示例 2:**

```
输入: 二叉树: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

输出: "1(2()(4))(3)"

解释: 和第一个示例相似，
除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。
```

## 思路

**DFS**

```
左子树不为空右子树为空，左右子树都为空，需要去掉空()，不影响映射。
```

## Python3 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def dfs(root):
            if not root:
                return ''
            # 左子树为空右子树不为空，要加一个()
            if not root.left and root.right:
                return str(root.val) + '()' + '(' + dfs(root.right) + ')'
            # 左子树不为空右子树为空
            elif root.left and not root.right:
                return str(root.val) + '(' + dfs(root.left) + ')'
            # 左右子树都为空
            elif not root.left and not root.right:
                return str(root.val)
            return str(root.val) + '(' + dfs(root.left) + ')' + '(' + dfs(root.right) + ')'
        
        return dfs(t)
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0606-Construct-String-from-Binary-Tree/0606.py)