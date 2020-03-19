> LeetCode 面试题32 - I. 从上到下打印二叉树【剑指Offer】【Medium】【Python】【二叉树】【BFS】

### 问题

[力扣](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树: `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回：

```
[3,9,20,15,7]
```

**提示：**

1. `节点总数 <= 1000`

### 思路

**BFS**

```
当队列不为空：
	队首元素出队，记为 node
	将 node.val 添加到 res 尾部
	若左（右）子节点不为空，则将左（右）子节点加入队列
```

**时间复杂度:** O(n)，n 为二叉树的节点数。
**空间复杂度:** O(n)，n 为二叉树的节点数。

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        import collections
        if not root:
            return []
        
        res, q = [], collections.deque()
        q.append(root)
        while q:
            node = q.popleft()  # O(1)
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-32-cong-shang-dao-xia-da-yin-er-cha-shu-lcof/32.py)