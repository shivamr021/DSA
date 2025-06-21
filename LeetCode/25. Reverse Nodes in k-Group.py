# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext
        return prev
        
    def findKthNode(self, temp, k):
        k -= 1
        while k and temp:
            k -= 1
            temp = temp.next
        return temp

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        temp = head
        prevLast = None
        while temp:
            kthNode = self.findKthNode(temp, k)
            
            if kthNode is None:
                if prevLast:
                    prevLast.next = temp
                break
            
            nextNode = kthNode.next
            kthNode.next = None
            
            self.reverseList(temp)

            if temp == head:
                head = kthNode
            else:
                prevLast.next = kthNode
            prevLast = temp
            temp = nextNode
        return head
