> LeetCode 0206. Reverse Linked List反转链表【Easy】【Python】【链表】

### Problem

[LeetCode](https://leetcode.com/problems/reverse-linked-list/)

Reverse a singly linked list.

**Example:**

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

**Follow up:**

A linked list can be reversed either iteratively or recursively. Could you implement both?

### 问题

[力扣](https://leetcode-cn.com/problems/reverse-linked-list/)

反转一个单链表。

**示例:**

```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```

**进阶:**
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

### 思路

##### 解法一

**栈**

```
普通数组模拟栈实现反转链表
```

**时间复杂度:** O(n)，n 为链表长度。
**空间复杂度:** O(n)，n 为链表长度。

##### Python3代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # solution one: List
        pos = head
        newList = []
        while pos:
            newList.insert(0, pos.val)
            pos = pos.next
        
        pos = head
        for _ in newList:
            pos.val = _
            pos = pos.next
        return head
```

##### 解法二

**双指针**

```
用 cur 和 pre 双指针实现反转链表。
可以动手在纸上画画，就能理解过程了。
```

**时间复杂度:** O(n)，n 为链表长度。
**空间复杂度:** O(1)

##### Python3代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # solution two: two point
        cur, pre = None, head
        while pre:
            pos = pre.next
            pre.next = cur
            cur = pre
            pre = pos
        return cur
```

##### 解法三

**递归**

```
直接利用递归实现反转链表。
```

**时间复杂度:** O(n)，n 为链表长度。
**空间复杂度:** O(1)

##### Python3代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # solution three: recursion
        if not head or not head.next:
            return head

        pos = head.next
        newList = self.reverseList(pos)

        head.next = None
        pos.next = head
        return newList
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0206-Reverse-Linked-List/0206.py)