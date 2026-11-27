# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        
        temp = head

        oddHead = ListNode(0)
        evenHead = ListNode(0)

        oddTemp = oddHead
        evenTemp = evenHead

        count = 1

        while temp is not None:
            if count % 2 != 0:
                oddTemp.next = ListNode(temp.data)
                oddTemp = oddTemp.next
            else:
                evenTemp.next = ListNode(temp.data)
                evenTemp = evenTemp.next

            temp = temp.next
            count += 1

        oddTemp.next = evenHead.next

        return oddHead.next
                




