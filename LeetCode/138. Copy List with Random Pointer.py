class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None  # Important check!

        curr = head 
        # Interweave original and copy list
        while curr:
            copiedNode = Node(curr.val, curr.next)
            curr.next = copiedNode
            curr = copiedNode.next 

        # Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Separate original and copied lists
        curr = head
        copy_head = head.next
        copy_curr = copy_head

        while curr:
            curr.next = curr.next.next
            if copy_curr.next:
                copy_curr.next = copy_curr.next.next
            curr = curr.next
            copy_curr = copy_curr.next

        return copy_head
