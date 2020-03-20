> LeetCode 面试题32 - II. 从上到下打印二叉树 II【剑指Offer】【Easy】【Python】【二叉树】【BFS】

### 问题

[力扣](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回其层次遍历结果：

```
[
  [3],
  [9,20],
  [15,7]
]
```

**提示：**

1. `节点总数 <= 1000`

注意：本题与主站 [102 题](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/) 相同

### 思路

**BFS**

```
当队列不为空：
	当前层打印循环：
		队首元素出队，记为 node
		将 node.val 添加到 temp 尾部
		若左（右）子节点不为空，则将左（右）子节点加入队列
	把当前 temp 中的所有元素加入 res
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        import collections
        if not root:
            return []
        
        res, q = [], collections.deque()
        q.append(root)
        while q:
            # 输出是二维数组
            temp = []
            for x in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        return res
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-32-cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/32-2.py)