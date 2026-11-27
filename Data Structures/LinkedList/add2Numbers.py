# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def addTwoNumbers(self, linkedList1: ListNode, linkedList2: ListNode) -> ListNode:
        sumHead = ListNode(0)
        temp = sumHead
        carry = 0

        while linkedList1 or linkedList2 or carry:
            val1 = linkedList1.data if linkedList1 else 0
            val2 = linkedList2.data if linkedList2 else 0

            sm = val1 + val2 + carry

            digit = sm % 10
            carry = sm // 10

            temp.next = ListNode(digit)
            temp = temp.next

            if linkedList1:
                linkedList1 = linkedList1.next

            if linkedList2:
                linkedList2 = linkedList2.next


        return sumHead.next
