> LeetCode 1367. Linked List in Binary Tree二叉树中的列表【Medium】【Python】【DFS】

### Problem

[LeetCode](https://leetcode.com/problems/linked-list-in-binary-tree/)

Given a binary tree `root` and a linked list with `head` as the first node. 

Return True if all the elements in the linked list starting from the `head` correspond to some *downward path* connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

**Example 1:**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/sample_1_1720.png)

```
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  
```

**Example 2:**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/sample_2_1720.png)

```
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
```

**Example 3:**

```
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
```

**Constraints:**

- `1 <= node.val <= 100` for each node in the linked list and binary tree.
- The given linked list will contain between `1` and `100` nodes.
- The given binary tree will contain between `1` and `2500` nodes.

### 问题

[力扣](https://leetcode-cn.com/problems/linked-list-in-binary-tree/)

给你一棵以 `root` 为根的二叉树和一个 `head` 为第一个节点的链表。

如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 `head` 为首的链表中每个节点的值，那么请你返回 `True` ，否则返回 `False` 。

一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。 

**示例 1：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/sample_1_1720.png)

```
输入：head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true
解释：树中蓝色的节点构成了与链表对应的子路径。
```

**示例 2：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/sample_2_1720.png)

```
输入：head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true
```

**示例 3：**

```
输入：head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：false
解释：二叉树中不存在一一对应链表的路径。
```

**提示：**

* 二叉树和链表中的每个节点的值都满足 `1 <= node.val <= 100` 。
* 链表包含的节点数目在 `1` 到 `100` 之间。
* 二叉树包含的节点数目在 `1` 到 `2500` 之间。

### 思路

**两重DFS**

```
第一重：找到起点。先判断当前节点，如果不对就判断左子树和右子树。
第二重：从找到的起点开始判断剩下的点。
```

##### Python3代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head == None:
            return True
        if root == None:
            return False
        # judge root, then judge root.left and root.right
        return self.isSub(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def isSub(self, head, node):
        # list is over
        if head == None:
            return True
        # list is not over and tree is over
        if node == None:
            return False
        # not equal
        if not head.val == node.val:
            return False
        # equal, then left and right
        return self.isSub(head.next, node.left) or self.isSub(head.next, node.right)
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1367-Linked-List-in-Binary-Tree/1367.py)

### 参考

[Jerry学长题解](https://leetcode-cn.com/problems/linked-list-in-binary-tree/solution/zhe-ti-jiu-shi-subtreeyi-mao-yi-yang-by-jerry_nju/)