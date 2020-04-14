# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = [], []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next

        temp = None
        carry = 0  # 进位
        
        while num1 or num2 or carry != 0:
            if not num1:
                a = 0
            else:
                a = num1.pop()
            if not num2:
                b = 0
            else:
                b = num2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            res = ListNode(cur)
            res.next = temp
            temp = res
        return res


if __name__ == "__main__":
    # l1 和 l2 写的有问题
    num1 = None
    l1 = ListNode(3)
    l1.next = num1
    num1 = l1
    l1 = ListNode(4)
    l1.next = num1
    num1 = l1
    l1 = ListNode(2)
    l1.next = num1
    num1 = l1
    l1 = ListNode(7)
    l1.next = num1

    num2 = None
    l2 = ListNode(4)
    l2.next = num2
    num2 = l2
    l2 = ListNode(6)
    l2.next = num1
    num2 = l2
    l2 = ListNode(5)
    l2.next = num2
    # num1 = ListNode(7)
    # l1 = ListNode(7)
    # l1.next = ListNode(2)
    # l1 = l1.next
    # l1.next = ListNode(4)
    # l1 = l1.next
    # l1.next = ListNode(2)
    # l1.next = None

    # num2 = ListNode(5)
    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2 = l2.next
    # l2.next = ListNode(4)
    # l2.next = None
    print(Solution().addTwoNumbers(l1, l2))