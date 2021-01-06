> LeetCode 0116. Populating Next Right Pointers in Each Node填充每个节点的下一个右侧节点指针【Medium】【Python】【Go】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

**Follow up:**

- You may only use constant extra space.
- Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

**Example 1:**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/116_sample.png)

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

## 问题

[力扣](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)

给定一个 **完美二叉树** ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```


填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

**进阶：**

- 你只能使用常量级额外空间。
- 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

**示例：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/116_sample.png)

```
输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
```

**提示：**

- 树中节点的数量少于 4096
- -1000 <= node.val <= 1000

## 思路

**递归**

```
通过构造辅助函数，将每一层节点连接起来转化成将每两个相邻节点连接起来。
```

### Python3 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # 将每两个相邻节点连接起来
        def connectTwoNode(node1: 'Node', node2: 'Node'):
            if not node1 or not node2:
                return
            
            node1.next = node2
            
            # 链接相同父节点的两个子节点
            connectTwoNode(node1.left, node1.right)
            connectTwoNode(node2.left, node2.right)
            # 链接不同父节点的两个子节点
            connectTwoNode(node1.right, node2.left)

        connectTwoNode(root.left, root.right)
        return root
```

### Go 代码

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */


 // 将每两个相邻节点连接起来
 func connectTwoNode(node1 *Node, node2 *Node) {
	 if node1 == nil && node2 == nil {
		 return
	 }
	 node1.Next = node2

	 // 链接相同父节点的两个子节点
	 connectTwoNode(node1.Left, node1.Right)
	 connectTwoNode(node2.Left, node2.Right)
	 // 链接不同父节点的两个子节点
	 connectTwoNode(node1.Right, node2.Left)
 }

 func connect(root *Node) *Node {
	if root == nil {
		return nil
	}

	connectTwoNode(root.Left, root.Right)
	return root
}
```

## GitHub 链接

- [Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0116-Populating-Next-Right-Pointers-in-Each-Node/0116.py)
- [Go](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0116-Populating-Next-Right-Pointers-in-Each-Node/0116.go)