# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next


class Solution:
    def deleteHead(self, head):
        if head is None:
            return head
        temp = head
        head = head.next 
        del temp
        return head
