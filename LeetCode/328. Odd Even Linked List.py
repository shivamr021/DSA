# Definition for singly-linked list.
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        oddDummy = Node(-1, None)
        evenDummy = Node(-1, None)

        odd = oddDummy
        even = evenDummy

        curr = head       
        cnt = 1
        while curr:
            if cnt % 2 == 1:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            curr = curr.next
            cnt += 1

        odd.next = evenDummy.next
        even.next = None
        return oddDummy.next
