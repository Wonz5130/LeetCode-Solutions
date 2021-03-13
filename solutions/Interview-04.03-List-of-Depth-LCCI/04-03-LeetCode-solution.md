> LeetCode 面试题 04.03. 特定深度节点链表【Medium】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/list-of-depth-lcci/)

给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

**示例：**


    输入：[1,2,3,4,5,null,7,8]
            1
           /  \ 
          2    3
         / \    \ 
        4   5    7
       /
      8
    
    输出：[[1],[2,3],[4,5,7],[8]]
## 思路

**BFS**

```
层次遍历，每层节点单独构成一个单链表。
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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        import collections

        if not tree:
            return []
        
        queue = collections.deque()
        queue.append(tree)
        res = []
        # BFS
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # 当前层的第一个节点
                if i == 0:
                    # 头节点
                    head = ListNode(node.val)
                    tmp = head
                else:
                    tmp.next = ListNode(node.val)
                    tmp = tmp.next
            # 这里加入res的是head
            res.append(head)
        return res
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/Interview-04.03-List-of-Depth-LCCI)