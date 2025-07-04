# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        t1, t2 = l1, l2
        head = tail = None
        carry = 0
        while t1 or t2 or carry:
            val1 = t1.val if t1 else 0
            val2 = t2.val if t2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            node = ListNode(total % 10)
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = node

            if t1: t1 = t1.next
            if t2: t2 = t2.next
        return head
