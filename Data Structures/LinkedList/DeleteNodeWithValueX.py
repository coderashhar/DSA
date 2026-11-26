# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def deleteNodeWithValueX(self, head: ListNode, x: int):
        """
            :type head: Optional[ListNode]
            :type x: int
            :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        
        temp = head

        if head.data == x:
            head = head.next
            return head

        while temp.next is not None and temp.next.data != x:
            temp = temp.next

        if temp.next is None:
            return head

        delNode = temp.next
        temp.next = temp.next.next
        del delNode

        return head
