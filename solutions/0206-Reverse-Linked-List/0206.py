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

        # solution two: two point
        cur, pre = None, head
        while pre:
            pos = pre.next
            pre.next = cur
            cur = pre
            pre = pos
        return cur

        # solution three: recursion
        if not head or not head.next:
            return head

        pos = head.next
        newList = self.reverseList(pos)

        head.next = None
        pos.next = head
        return newList