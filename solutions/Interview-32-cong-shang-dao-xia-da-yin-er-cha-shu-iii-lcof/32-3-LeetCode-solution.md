> LeetCode 面试题32 - III. 从上到下打印二叉树 III【剑指Offer】【Medium】【Python】【二叉树】【BFS】

### 问题

[力扣](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

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
  [20,9],
  [15,7]
]
```

**提示：**

1. `节点总数 <= 1000`

### 思路

**BFS**

```
当队列不为空：
	当前层打印循环：
		队首元素出队，记为 node
		根据 flag 将 node.val 添加到 temp 尾部/头部
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
        # 做奇偶判断
        flag = False
        q.append(root)
        while q:
            # 输出是二维数组
            temp = []
            flag = not flag
            for x in range(len(q)):
                node = q.popleft()
                # 尾插
                if flag:
                    temp.append(node.val)
                # 头插
                else:
                    temp.insert(0, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        return res
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-32-cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/32-3.py)