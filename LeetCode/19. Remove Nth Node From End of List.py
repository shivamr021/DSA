# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        fast = head
        for _ in range(n):
            fast = fast.next
        
        if fast is None:
            return head.next

        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return head
