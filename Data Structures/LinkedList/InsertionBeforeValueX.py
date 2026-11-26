# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def insertBeforeX(self, head: ListNode, x: int, val: int):
        """
            :type head: Optional[ListNode]
            :type x: int
            :type val: int
            :rtype: Optional[ListNode]
        """
        newNode = ListNode(val)

        if head is None:
            return head

        if head.data == x:
            newNode.next = head
            return newNode

        temp = head

        while temp.next is not None and temp.next.data != x:
            temp = temp.next
        
        if temp.next is None:
            return head

        temp2 = temp.next
        temp.next = newNode
        newNode.next = temp2

        return head


