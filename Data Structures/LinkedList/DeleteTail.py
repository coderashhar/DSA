# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def deleteTail(self, head: ListNode):
        """
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        
        temp = head

        while temp.next.next is not None:
            temp = temp.next
        
        delNode = temp.next
        del delNode

        temp.next = None
        
        return head
    
