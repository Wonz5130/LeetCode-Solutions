# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # solution one: reverse
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.reverse()
        return res

        # solution two: 栈
        stack = []
        while head:  # push
            stack.append(head.val)
            head = head.next
        res = []
        while stack:  # pop
            res.append(stack.pop())
        return res

        # solution three: 递归
        return self.reversePrint(head.next) + [head.val] if head else []