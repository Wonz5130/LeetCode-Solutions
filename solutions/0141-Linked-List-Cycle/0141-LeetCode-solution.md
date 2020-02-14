> LeetCode 0141. Linked List Cycle环形链表【Easy】【Python】【双指针】

### 题目

[英文题目地址](https://leetcode.com/problems/linked-list-cycle/)

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where tail connects to. If `pos` is `-1`, then there is no cycle in the linked list.

**Example 1:**

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Example 2:**

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Example 3:**

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

 

**Follow up:**

Can you solve it using *O(1)* (i.e. constant) memory?

### 翻译

[中文题目地址](https://leetcode-cn.com/problems/linked-list-cycle/)

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 `pos` 是 `-1`，则在该链表中没有环。

**示例 1：**

```
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**示例 2：**

```
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**示例 3：**

```
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

**进阶：**

你能用 *O(1)*（即，常量）内存解决此问题吗？

### 思路

**双指针**

用 fast 和 slow 快慢双指针，fast 指针速度设为 slow 速度的两倍，如果链表有环，则快慢双指针必会相遇，[证明请看这里](https://blog.csdn.net/jnxxhzz/article/details/82773112)。

**空间复杂度**: O(1)

### Python代码

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow, fast = head, head  # 快慢双指针
        while fast.next != None and fast.next.next != None:  # 一定是 fast.next 和 fast.next.next
            slow = slow.next
            fast = fast.next.next  # fast快指针速度是slow慢指针的两倍
            if slow == fast:  # 如果链表有环, fast 和 slow 必会相遇
                return True
        return False
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0141-Linked-List-Cycle/0141.py)