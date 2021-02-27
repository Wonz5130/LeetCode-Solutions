> LeetCode 0662. Maximum Width of Binary Tree 二叉树最大宽度【Medium】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/maximum-width-of-binary-tree/)

给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。

每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。

**示例 1:**

    输入: 
    	   1
         /   \
        3     2
       / \     \  
      5   3     9 
    
    输出: 4
    解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。

**示例 2:**

    输入: 
    	  1
         /  
        3    
       / \       
      5   3   
    
    输出: 2
    解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。

**示例 3:**

    输入: 
    	  1
         / \
        3   2 
       /        
      5      
    
    输出: 2
    解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。

**示例 4:**

    输入: 
     	  1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
    
    输出: 8
    解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
**注意:** 答案在32位有符号整数的表示范围内。

## 思路

**BFS**

```
满二叉树的特性：节点p的左子节点的序号为2p，右子节点的序号为2p+1。
同一层中，首末元素的坐标差就是最大宽度。
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
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 分别是坐标和节点
        queue = [(0, root)]
        res = 1
        # BFS
        while queue:
            # 首末元素的坐标差就是最大宽度
            res = max(res, queue[-1][0] - queue[0][0] + 1)
            tmp = []
            for i, q in queue:
                if q.left:
                    tmp.append((i * 2, q.left))
                if q.right:
                    tmp.append((i * 2 + 1, q.right))
            queue = tmp
        return res
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/0662-Maximum-Width-of-Binary-Tree)