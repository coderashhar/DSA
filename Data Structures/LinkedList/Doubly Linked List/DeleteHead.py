"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def deleteHead(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None

        temp = head
        head = head.next
        head.prev = None
        temp.next = None

        return head
