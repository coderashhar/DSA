"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def deleteTail(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        
        temp = head
        while temp.next is not None:
            temp = temp.next

        temp2 = temp.prev
        temp.prev = None 
        temp2.next = None

        return head