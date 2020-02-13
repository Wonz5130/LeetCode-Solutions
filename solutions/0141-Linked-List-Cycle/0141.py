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