class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        temp = head
        while temp:
            currNext = temp.next
            temp.next = prev
            prev = temp
            temp = currNext
        return prev
