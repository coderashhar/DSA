"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def insertBeforeTail(self, head: ListNode, X: int) -> ListNode:
        newNode = ListNode(X)

        if head is None:
            return newNode
        
        if head.next is None:
            head.prev = newNode
            newNode.next = head
            return newNode
        
        temp = head
        while temp.next.next is not None:
            temp = temp.next
        
        temp2 = temp.next
        temp.next = newNode
        newNode.prev = temp
        newNode.next = temp2
        temp2.prev = newNode

        return head