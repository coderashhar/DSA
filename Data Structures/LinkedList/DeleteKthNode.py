# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def deleteKthNode(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None

        temp = head 

        if k == 1:
            head = head.next
            del temp
            return head

        while temp.next is not None and k > 2:
            temp = temp.next
            k -= 1

        delNode = temp.next
        temp.next = temp.next.next
        del delNode

        return head
