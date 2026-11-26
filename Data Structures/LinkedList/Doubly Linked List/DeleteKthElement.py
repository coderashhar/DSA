"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def deleteKthElement(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        if k == 1:
            head = head.next
            if head is not None:
                head.prev = None
            return head

        temp = head
        while temp.next is not None and k > 2:
            temp = temp.next
            k -= 1

        temp2 = temp.next
        temp.next = temp.next.next
        if temp.next is None:
            return head
        temp.next.prev = temp

        temp2.next = None
        temp2.prev = None

        return head
