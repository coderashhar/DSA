# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def insertAtTail(self, head: ListNode, x: int):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        newNode = ListNode(x)
        if head == None:
            return newNode
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
        newNode.next = None
        return head