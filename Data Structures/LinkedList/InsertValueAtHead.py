# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def insertAtHead(self, head: ListNode, x: int):
        """
            :type head: Optional[ListNode]
            :type x: int
            :rtype: Optional[ListNode]
        """
        newNode = ListNode(x)

        if head is None:
            return newNode
        
        temp = head 
        newNode.next = temp
        head = newNode

        return head