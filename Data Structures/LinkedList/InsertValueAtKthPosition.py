# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def insertAtKthPosition(self, head: ListNode, x: int, k):
        """
            :type head: Optional[ListNode]
            :type x: int
            :rtype: Optional[ListNode]
        """
        newNode = ListNode(x)

        if k == 1:
            newNode.next = head
            head = newNode
            return head

        temp = head

        while temp.next is not None and k > 2:
            temp = temp.next
            k -= 1
        
        temp2 = temp.next
        temp.next = newNode
        newNode.next = temp2

        return head